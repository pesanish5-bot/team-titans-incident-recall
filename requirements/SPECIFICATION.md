# HackwithHyderabad 3.0 — Local Specification

This is a faithful, implementation-oriented extraction of the supplied official problem statement and content guide, accessed on 29 September 2026. It separates explicit requirements from recommendations and flags source inconsistencies rather than inventing resolutions.

## 1. Project objective

Build an AI-powered application using **Hindsight**, Vectorize's memory system, so that an AI agent can remember, recall, and improve over time. The solution must demonstrate persistent memory and learning from past interactions rather than behaving as a stateless chatbot.

The recommended project shape is deliberately narrow:

- Solve a real business problem that someone could plausibly pay to solve.
- Make memory central and visible, not an incidental feature.
- Pick one workflow, one persona, and one clear value proposition.
- Show an obvious, realistic before/after story in approximately 60 seconds.
- Demonstrate improvement across interactions, long-term context recall, learned preferences, or accumulated domain expertise.
- Prefer a polished single-purpose agent over a broad, shallow prototype.
- Avoid student-centric concepts such as tutors, group-project managers, and quiz generators.
- Use realistic data; public datasets or realistic synthetic data are acceptable recommendations in the source.

The source lists examples in sales, marketing, engineering/DevOps, operations/support, and product/strategy. These are inspiration only; **no specific product idea has been selected for this repository**.

## 2. Required technology

- Every team must use Hindsight.
- The project must clearly demonstrate how Hindsight memory is used.
- The submission must explain how Hindsight memory is used in the solution.
- Teams may use Hindsight Cloud or the open-source version.
- The source provides promo code `MEMHACK99` for $50 in Hindsight Cloud credits, to be added in billing after registration.
- Any LLM may be used. The source recommends Groq and mentions `openai/gpt-oss-120b` and `qwen/qwen3-32b`, with a warning that the agent should handle function-calling errors.
- OpenClaw is optional; an official Hindsight integration is linked in `SOURCES.md`.

No programming language, UI framework, hosting platform, model provider, or deployment architecture is mandated in the supplied documents.

## 3. Required submission package

Each team must submit:

- A GitHub repository with clean, documented code.
- A demo video showing the agent in action.
- A live project demo to judges.
- An explanation of how Hindsight memory is used.
- Content deliverables described by the official content guide.

Operational requirements supplied with this workspace:

- **Every team member must complete the [Profile Review Form](https://forms.gle/AXWnanWsEEir6xSP9).**
- **Only one final team submission is allowed through the [Final Submission Form](https://forms.gle/cD7fCnPnkdVm2sH78).**
- Announced submission date: **29 September 2026**. No time or timezone was supplied.

## 4. Judging criteria

| Criterion | Weight | Evidence judges seek |
| --- | ---: | --- |
| Innovation | 30% | A fresh take on a real problem that goes beyond an obvious chatbot |
| Use of Hindsight Memory | 25% | Memory is central; the agent clearly improves over time |
| Technical Implementation | 20% | Clean, well-architected, functional code that handles edge cases |
| User Experience | 15% | Intuitive interaction and a compelling demo flow |
| Real-world Impact | 10% | A genuine problem, real users, and a path to adoption |

## 5. Content-contest eligibility and ownership

The content guide states that a team is eligible for the team content contest when:

- Every team member publishes one English-language technical article.
- Every team member publishes one English-language social post promoting their article.
- The team publishes one shared video.

Team members may cover the same project from different angles or focus on their own contributions.

The problem statement's submission section instead says that all team members must complete an Article, Social Media post, **and Video**. This conflicts with the content guide's clearer table saying one video per team. Treat this as an organizer clarification item; the safer interpretation for planning is one team video plus individual articles and social posts, while confirming whether any individual video requirement exists.

## 6. Article requirements

### Publication and subject

- Publish in English at a public, linkable URL where developers can find it.
- Suggested platforms: Medium, Dev.to, Hashnode, Substack, or LinkedIn Articles.
- Do not submit a Google Drive document link as the published artifact.
- Frame the story around the idea, outcome, or a concrete engineering insight—not the event.
- **Do not mention the hackathon anywhere in the article title or body, including hashtags; the guide says this causes disqualification.**
- Mention Hindsight positively and make its use and benefits a major theme.
- Ground claims, examples, and code snippets in the actual repository. Do not invent benchmarks or unsupported results.
- Write in a first-person, technically credible, concrete voice without hype or marketing buzzwords.
- Add project screenshots, terminal/code screenshots, an architecture diagram, and optionally a team photo.

### Required article evidence and links

The guide's pre-submit checklist requires:

- A title about the idea/result rather than the event.
- A specific, surprising opening rather than a generic introduction.
- A concrete explanation of the problem.
- A clear account of where and how Hindsight is integrated.
- At least one real code snippet from the project.
- At least one concrete before/after example.
- At least one honest lesson, limitation, or dead end.
- Screenshots or images.
- A public, linkable publication URL.

Embed these links naturally with useful anchor text:

- `https://github.com/vectorize-io/hindsight`
- `https://hindsight.vectorize.io/`
- `https://vectorize.io/what-is-agent-memory`

### Article length inconsistency

- The content-contest table says **800–1,500 words**.
- The full-article prompt says **1,200–2,000 words**.
- The quick-reference section again says **800–1,500 words**.

Until clarified, target **1,200–1,500 words**, which satisfies both ranges.

### Recommended structure from the supplied prompt

1. Hook in the first one or two sentences.
2. What the system does and how it fits together.
3. One deep, opinionated technical through-line.
4. Two to four small repository-backed code snippets (while the checklist requires at least one).
5. Results or behavior shown with concrete example interactions.
6. Three to five reusable lessons.

The guide asks authors to edit AI-generated drafts, add their own voice, verify details, add visuals, and check platform formatting before publication.

## 7. Social post requirements

- Each team member publishes a LinkedIn post promoting their published article; the prompt may be adjusted for X.
- Talk about the useful project and concrete practitioner value, not the event.
- **Do not mention the hackathon anywhere in the post, including hashtags; the guide says this causes disqualification.**
- Keep the generated LinkedIn post under 800 characters.
- Put a bold or curiosity-driving hook in the first two lines; do not put hashtags or links in those lines.
- Use short, mobile-friendly paragraphs.
- Include three to seven concrete technical takeaways or before/after contrasts.
- Include at least one behavior change from before to after adding the technology.
- Positively mention Hindsight agent memory and the decision to use it.
- Include the project GitHub link in the main post.
- Put three to five relevant hashtags on the last line only. The guide offers `#AIAgents`, `#AI`, `#Hindsight`, `#AgentMemory`, `#AIMemory`, and `#LLM`; do not use event- or student-related tags.
- Put the published article URL in the first comment.
- Add another comment linking to `https://github.com/vectorize-io/hindsight`.

The guide additionally says to tag Code.in on LinkedIn and in articles.

## 8. Video requirements

- Publish one team demo video publicly on YouTube; do not submit only a Google Drive link.
- Length: **2–5 minutes**, with shorter preferred.
- Resolution: **1080p minimum**.
- Record the screen directly, not by pointing a phone at it.
- Screen recording with voiceover is acceptable; talking head plus screen recording is preferred but not mandatory.
- Show retain/recall happening live.
- Use a 16:9, attention-grabbing thumbnail; the guide recommends generating it with Google Nano Banana and supplying a team-member photo.

Suggested flow:

1. Quick introduction: who you are, what you built, and why (about 30 seconds).
2. The problem: show failure or struggle without memory (about 30 seconds).
3. Live demo: a real interaction with retain/recall and a before/after moment (about 2–3 minutes).
4. Wrap-up: one key takeaway and what surprised you (about 30 seconds).

The source's nominal timings can total four minutes, despite calling its optional generated script a three-minute script. Keep the final recording within the explicit 2–5 minute requirement.

## 9. Content-guide numbering inconsistencies

The detailed guide labels prompts as 1, 2, 3, 5, and 6, while its quick reference calls the video-script prompt 4 and the thumbnail prompt 5. It also says the title prompt generates 5 ideas in the quick reference, while the actual title prompt requires exactly 20 titles. Follow the detailed prompt bodies unless organizers clarify otherwise.

## 10. Acceptance criteria for the software

Before calling the implementation submission-ready, the team should be able to demonstrate all of the following:

- Hindsight is present in the actual runtime path, not only named in documentation.
- The agent retains information from one interaction and recalls it in a later interaction.
- Memory produces a visible, useful behavior change compared with the same workflow without memory.
- The demo has a deterministic or reliably repeatable setup that fits into a 60-second core story.
- Function/tool-call failures and unavailable external services have understandable handling.
- Data used in the demo is realistic and safe to publish.
- Setup instructions allow a reviewer to run the project.
- The repository is clean and documented, and the live demo works.
- The content package accurately reflects the implemented code and does not invent results.

## 11. Open decisions (not specified by the sources)

The team must supply these before implementation:

- Chosen business problem and why it matters.
- Primary persona and one narrow workflow.
- The memory learning loop: what is retained, when it is recalled, and how behavior changes.
- The exact before/after demo scenario and evidence.
- Team roster and content ownership.
- Hindsight Cloud versus open-source deployment.
- LLM/provider choice.
- UI, backend, persistence, hosting, and authentication choices.
- Data source and privacy/redaction plan.
- Final submission deadline time and timezone.
- Clarification of the individual-versus-team video inconsistency.
