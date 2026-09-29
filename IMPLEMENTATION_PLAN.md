# Implementation Plan

Status: **Product decision approved; implementation in progress.**

Approved concept: an incident response memory agent for TEAM TITANS. One on-call engineer records a verified root cause and mitigation, then recalls them when a similar alert fires. The 60-second demo is: brief an alert with empty memory, retain a resolved incident, and brief the same symptoms again. Improvement is evidenced by the specific recalled cause and mitigation, not an invented performance metric.

The first implementation uses a small Python web server and Hindsight HTTP API. Each service has its own memory bank. The UI compares a generic triage checklist with recalled incident evidence. Examples are synthetic until approved real cases are supplied. Do not enter secrets or customer data.

Team: Anish Bhowmick, Akshyat Kumar Nayak, Devaans Patwari, Abhishek Dutta.

Remaining gates: live Hindsight retain/recall verification, approved demo data, published repository, individual articles and posts, team video, Reddit link, and agreement on the single final submission.

The official sources require a Hindsight-powered application but do not choose the problem, persona, or workflow. Architecture should follow those choices, not precede them.

## Phase 0 — Product decision gate

Complete and review this brief:

| Decision | Team answer |
| --- | --- |
| Real business problem | TBD |
| Primary user/persona | TBD |
| Single narrow workflow | TBD |
| Why someone would pay for it | TBD |
| What the agent retains | TBD |
| When and how it recalls memory | TBD |
| Behavior without memory | TBD |
| Behavior after repeated interactions | TBD |
| 60-second judge demo | TBD |
| Evidence of improvement | TBD |
| Realistic/synthetic data source | TBD |
| Sensitive-data handling | TBD |
| Team members and owners | TBD |

Selection test: choose a concept only if memory is essential to its value, the difference is visible quickly, the scope can be polished in the available time, and the team would credibly use or showcase it.

**Exit condition:** the team has approved one completed row set above and can narrate the before/after demo without discussing implementation details.

## Phase 1 — Technical spike and architecture proposal

After Phase 0, evaluate only what the chosen workflow needs:

1. Test the smallest retain/recall round trip against Hindsight Cloud or open source.
2. Verify the chosen LLM's tool/function-calling behavior and define recovery paths.
3. Map the memory lifecycle: subject/bank identity, retained facts or episodes, recall query, ranking/use, correction, and deletion/reset for demos.
4. Decide the minimum UI and service boundaries.
5. Document environment variables without committing secrets.
6. Define an offline or degraded-mode message for external-service failures.

Deliverable: a short architecture decision record plus a tested Hindsight spike. Do not build broad product features during the spike.

## Phase 2 — Thin vertical slice

Build one end-to-end path:

1. User starts the chosen workflow.
2. Agent responds without relevant prior memory.
3. A meaningful event is retained in Hindsight.
4. A later interaction recalls it.
5. The response changes in a way the user can see and verify.

Add traceability sufficient for the demo to show retain and recall without exposing secrets or private chain-of-thought.

Deliverable: a runnable 60-second before/after scenario.

## Phase 3 — Reliability and judging coverage

- Add tests for memory identity/isolation, empty recall, duplicate retention, malformed tool calls, unavailable services, and reset/replay behavior.
- Make demo data realistic and repeatable.
- Refine the interaction so the value is understandable without narration.
- Check work against all five judging criteria in `requirements/SPECIFICATION.md`.
- Write clean setup, configuration, usage, and architecture documentation.

Deliverable: submission-quality repository and reliable live demo.

## Phase 4 — Evidence and submission assets

- Capture real UI, terminal, and architecture visuals.
- Record the public 2–5 minute, 1080p-minimum YouTube demo.
- Each team member writes and publishes an English article and social post, following the event-reference prohibition in the official content guide.
- Ensure the article contains repository-backed snippets and concrete before/after evidence.
- Add the project repository link to the main social post, the article URL to its first comment, and the Hindsight repository link in a comment.
- Have every team member complete the Profile Review Form.
- Designate one owner to make the single final team submission.

Deliverable: verified public URLs and one final team submission checklist.

## Phase 5 — Final verification

- Re-read the official documents for updates.
- Confirm the exact deadline time and timezone.
- Confirm whether the apparent video-ownership conflict requires any additional individual video.
- Verify every link in a signed-out/private browser window.
- Run the demo from a clean setup.
- Check that public content contains no secrets, private data, invented metrics, or prohibited event references.
- Submit once and record the receipt/confirmation.

## Stop conditions

Do not scaffold the application, add dependencies, or select a technology stack until Phase 0 is complete. Do not generate final content assets until the implementation exists; the official guide requires them to be grounded in the actual repository and behavior.
