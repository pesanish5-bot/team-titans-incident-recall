import json
import unittest
from unittest.mock import patch

from app import AppError, Hindsight, bank_id, create_brief, record_incident


class FakeResponse:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def read(self):
        return json.dumps(self.value).encode()


class IncidentRecallTests(unittest.TestCase):
    def setUp(self):
        self.calls = []
        self.memories = {}
        self.memory = Hindsight("https://example.test", "test-key")

    def fake_urlopen(self, request, timeout):
        data = json.loads(request.data)
        self.calls.append((request.get_method(), request.full_url, data, request.get_header("Authorization")))
        bank = request.full_url.split("/banks/", 1)[1].split("/", 1)[0]
        if request.full_url.endswith("/memories/recall"):
            return FakeResponse({"results": [{"text": item} for item in self.memories.get(bank, [])]})
        if request.full_url.endswith("/memories"):
            self.memories.setdefault(bank, []).extend(item["content"] for item in data["items"])
        return FakeResponse({"ok": True})

    def test_retain_then_recall_is_service_scoped(self):
        with patch("app.urlopen", side_effect=self.fake_urlopen):
            record_incident({
                "service": "checkout-api",
                "symptoms": "502s after deploy",
                "cause": "Connection pool exhausted",
                "mitigation": "Raised pool limit to 80",
                "followup": "Add saturation alert",
            }, self.memory)
            remembered = create_brief({"service": "checkout-api", "symptoms": "502s"}, self.memory)
            other = create_brief({"service": "billing-api", "symptoms": "502s"}, self.memory)
        self.assertIn("Connection pool exhausted", remembered["memories"][0]["text"])
        self.assertIn("Raised pool limit to 80", remembered["memories"][0]["text"])
        self.assertEqual(other["memories"], [])
        self.assertEqual(remembered["bank"], bank_id("checkout-api"))
        self.assertTrue(any(method == "PUT" and url.endswith("/banks/team-titans-incident-checkout-api") for method, url, _, _ in self.calls))
        self.assertTrue(any(method == "POST" and url.endswith("/memories/recall") for method, url, _, _ in self.calls))
        self.assertTrue(all(auth == "Bearer test-key" for _, _, _, auth in self.calls))

    def test_requires_verified_fields_before_retaining(self):
        with self.assertRaises(AppError):
            record_incident({"service": "checkout-api", "symptoms": "502s"}, self.memory)
        self.assertEqual(self.calls, [])


if __name__ == "__main__":
    unittest.main()
