# Synthetic incident replay

All names and incidents below are invented for a repeatable demonstration.

## First alert: no prior memory

In **Brief a new alert**, enter:

- Service: `checkout-api`
- Current symptoms: `502 errors rise during checkout after a deploy; database connections are saturated`

With a fresh service bank, Hindsight should return no relevant incident. The interface shows only the baseline triage steps.

## Resolved incident: retain

In **Record resolved incident**, enter:

- Service: `checkout-api`
- Symptoms: `502 errors rose during checkout after a deploy; database connections reached the configured pool limit`
- Verified root cause: `The new checkout worker count exhausted the database connection pool`
- Successful mitigation: `Reduced checkout workers and raised the pool limit after checking database capacity`
- Follow-up: `Add a connection saturation alert and cap worker count in deployment checks`

Press **Retain incident** and wait for the success message. This must be backed by a live Hindsight instance for the final demo.

## Later alert: recall

Brief the same service with similar symptoms. Compare the returned memory evidence with the earlier baseline. Verify the text reflects the stored incident; Hindsight may paraphrase it. Do not claim a specific memory count or exact wording until the live run has been recorded.

## Safety of the demo

Do not execute mitigation steps against a real environment. This scenario demonstrates how prior incident evidence reaches an engineer, not an automated production change.
