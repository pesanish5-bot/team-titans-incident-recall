"""Incident Recall: a small web app backed by Hindsight memory."""

from __future__ import annotations

import json
import os
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

WEB = Path(__file__).resolve().parent / "web"
BASELINE = [
    "Confirm the alert and current user impact.",
    "Check recent deploys, configuration changes, and dependency health.",
    "Review logs and metrics before applying a mitigation.",
    "Escalate through the service runbook if the cause remains unclear.",
]


class AppError(Exception):
    def __init__(self, message: str, status: int = 400):
        super().__init__(message)
        self.status = status


def clean_text(value: object, label: str, limit: int = 1500) -> str:
    if not isinstance(value, str):
        raise AppError(f"{label} must be text.")
    text = value.strip()
    if not text:
        raise AppError(f"{label} is required.")
    if len(text) > limit:
        raise AppError(f"{label} must be {limit} characters or fewer.")
    return text


def bank_id(service: str) -> str:
    service = clean_text(service, "Service", 80)
    slug = re.sub(r"[^a-z0-9]+", "-", service.lower()).strip("-")
    if not slug:
        raise AppError("Service must include a letter or number.")
    prefix = re.sub(r"[^a-z0-9-]+", "-", os.getenv("INCIDENT_RECALL_PREFIX", "team-titans").lower()).strip("-")
    return f"{prefix or 'team-titans'}-incident-{slug}"


def incident_narrative(data: dict) -> str:
    fields = {
        "Service": clean_text(data.get("service"), "Service", 80),
        "Symptoms": clean_text(data.get("symptoms"), "Symptoms"),
        "Verified root cause": clean_text(data.get("cause"), "Root cause"),
        "Successful mitigation": clean_text(data.get("mitigation"), "Mitigation"),
        "Follow-up": clean_text(data.get("followup"), "Follow-up"),
    }
    return "Resolved production incident. " + " ".join(f"{key}: {value}." for key, value in fields.items())


class Hindsight:
    def __init__(self, base_url: str | None = None, api_key: str | None = None):
        self.base_url = (base_url or os.getenv("HINDSIGHT_API_URL", "http://localhost:8888")).rstrip("/")
        self.api_key = api_key if api_key is not None else os.getenv("HINDSIGHT_API_KEY", "")
        parsed = urlparse(self.base_url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise AppError("HINDSIGHT_API_URL must be an HTTP(S) URL.", 500)

    def request(self, method: str, path: str, payload: dict) -> dict:
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        request = Request(
            f"{self.base_url}{path}",
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method=method,
        )
        try:
            with urlopen(request, timeout=25) as response:
                raw = response.read()
                return json.loads(raw) if raw else {}
        except HTTPError as exc:
            if exc.code in (401, 403):
                raise AppError("Hindsight rejected the API key. Check server configuration.", 502) from exc
            if exc.code == 404:
                raise AppError("Hindsight could not find the requested memory bank or API route.", 502) from exc
            raise AppError(f"Hindsight returned HTTP {exc.code}.", 502) from exc
        except (URLError, TimeoutError, OSError) as exc:
            raise AppError("Hindsight is unreachable. Check HINDSIGHT_API_URL and the server.", 503) from exc
        except json.JSONDecodeError as exc:
            raise AppError("Hindsight returned an invalid response.", 502) from exc

    def ensure_bank(self, bank: str) -> None:
        self.request("PUT", f"/v1/default/banks/{quote(bank)}", {})

    def retain(self, bank: str, content: str) -> dict:
        self.ensure_bank(bank)
        return self.request("POST", f"/v1/default/banks/{quote(bank)}/memories", {"items": [{"content": content}]})

    def recall(self, bank: str, query: str) -> list[dict]:
        self.ensure_bank(bank)
        response = self.request("POST", f"/v1/default/banks/{quote(bank)}/memories/recall", {"query": query})
        results = response.get("results", [])
        if not isinstance(results, list):
            raise AppError("Hindsight returned an unexpected recall result.", 502)
        memories = []
        for item in results[:5]:
            if isinstance(item, dict) and isinstance(item.get("text"), str) and item["text"].strip():
                memories.append({"text": item["text"].strip()})
        return memories


def record_incident(data: dict, memory: Hindsight) -> dict:
    if not isinstance(data, dict):
        raise AppError("A JSON object is required.")
    bank = bank_id(data.get("service"))
    memory.retain(bank, incident_narrative(data))
    return {"bank": bank, "message": "Incident retained in Hindsight."}


def create_brief(data: dict, memory: Hindsight) -> dict:
    if not isinstance(data, dict):
        raise AppError("A JSON object is required.")
    service = clean_text(data.get("service"), "Service", 80)
    symptoms = clean_text(data.get("symptoms"), "Symptoms")
    bank = bank_id(service)
    query = f"For the {service} service, which prior production incidents involved {symptoms}? Recall verified causes and successful mitigations."
    memories = memory.recall(bank, query)
    return {"service": service, "bank": bank, "baseline": BASELINE, "memories": memories}


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:
        if self.path not in ("/api/incidents", "/api/brief"):
            self.send_json(404, {"error": "Not found."})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length < 1 or length > 25000:
                raise AppError("Request body must be between 1 and 25,000 bytes.")
            data = json.loads(self.rfile.read(length))
            memory = Hindsight()
            result = record_incident(data, memory) if self.path == "/api/incidents" else create_brief(data, memory)
            self.send_json(200, result)
        except json.JSONDecodeError:
            self.send_json(400, {"error": "Invalid JSON."})
        except (TypeError, ValueError) as exc:
            self.send_json(400, {"error": str(exc)})
        except AppError as exc:
            self.send_json(exc.status, {"error": str(exc)})

    def do_GET(self) -> None:
        paths = {"/": ("index.html", "text/html"), "/app.js": ("app.js", "text/javascript"), "/style.css": ("style.css", "text/css")}
        route = paths.get(self.path)
        if route is None:
            self.send_error(404)
            return
        path, content_type = route
        body = (WEB / path).read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8765"))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"Incident Recall is running at http://localhost:{port}")
    server.serve_forever()
