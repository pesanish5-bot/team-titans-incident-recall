# Incident Recall — HackwithHyderabad 3.0

Isolated, documentation-first workspace for the Hindsight agent-memory hackathon.

## Current status

- The official problem statement and content guide were accessible through their public, read-only Google Docs text exports on 29 September 2026.
- Their requirements have been captured in [`requirements/SPECIFICATION.md`](requirements/SPECIFICATION.md).
- The team selected an incident response memory agent for on-call engineers.
- Implementation status and remaining gates are in [`IMPLEMENTATION_PLAN.md`](IMPLEMENTATION_PLAN.md).

## Mandatory team actions

> **Every team member must complete the [Profile Review Form](https://forms.gle/AXWnanWsEEir6xSP9).**
>
> **Only one final team submission is allowed via the [Final Submission Form](https://forms.gle/cD7fCnPnkdVm2sH78).**

The announced submission date supplied with this workspace is **29 September 2026**. The source documents captured here do not state a submission time or timezone, so the team should confirm those details with the organizers.

## Start here

1. Read [`requirements/SPECIFICATION.md`](requirements/SPECIFICATION.md).
2. Set `HINDSIGHT_API_URL` to your Hindsight server (Cloud: `https://api.hindsight.vectorize.io`; local: `http://localhost:8888`).
3. Set `HINDSIGHT_API_KEY` for Cloud. Keep keys out of Git.
4. Run `python app.py` and open `http://localhost:8765`.
5. Record a resolved incident, then brief a similar alert.

Python 3.10+ is sufficient; no package installation is required. Run `python -m unittest discover -s tests -v` for the included request-flow tests. The app reports Hindsight connection errors and does not invent memory results.

The app sends resolved incident text to Hindsight `retain` and calls `recall` for a new alert, using a separate memory bank per service. It shows retrieved evidence beside a generic baseline checklist. Recalled content is advisory and must be reviewed before acting.

Source links and access notes are in [`requirements/SOURCES.md`](requirements/SOURCES.md).
