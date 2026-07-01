# Portfolio Roadmap

Ideas for future repositories that would strengthen a professional portfolio in enterprise AI implementation. Each project is tied to a real operational problem — not an isolated coding exercise.

---

## Principles for portfolio projects

Every repository in this portfolio should:

1. **Start with a business problem** — name who feels the pain and why it matters
2. **Show discovery thinking** — explain what was understood before building
3. **Use AI purposefully** — justify why AI fits, not just that it was used
4. **Include a runnable artifact** — code, workflow export, or template someone can interact with
5. **Document lessons learned** — what worked, what didn't, what would change next time
6. **Stay honest about scope** — prototype vs. production, clearly labeled

---

## Suggested repositories

### AI Discovery Assistant

**Problem:** Enterprise AI projects often stall because teams jump to solutions before mapping workflows, stakeholders, and success criteria.

**What it could contain:** A structured discovery template (questionnaire + output format) that guides teams through workflow mapping, pain point identification, AI fit assessment, and success metric definition. Possibly a lightweight tool that generates a discovery brief from structured inputs.

**Why it fits the portfolio:** Demonstrates that implementation starts with understanding — the skill that separates senior customer-facing roles from pure engineering.

---

### Executive Brief Generator

**Problem:** After discovery workshops or POC results, someone needs to translate technical findings into a concise executive summary — often under time pressure.

**What it could contain:** A prompt framework + example workflow that takes structured discovery notes or POC outcomes and produces a one-page executive brief: problem, approach, results, recommendation, next steps.

**Why it fits the portfolio:** Shows ability to bridge technical work and executive communication — critical for deployment strategist and solutions architect roles.

---

### Customer Health Agent

**Problem:** Customer success teams monitor dozens of accounts but lack automated early signals when an account shows risk (usage drop, support ticket spike, missed milestones).

**What it could contain:** An event-driven workflow prototype that ingests account signals, applies AI to classify health status, and posts a summary to the account owner's workspace — with explicit human-in-the-loop review before escalation.

**Why it fits the portfolio:** Demonstrates post-sale operational AI — a different lifecycle stage from the sales intelligence track, showing breadth.

---

### AI Implementation Playbooks

**Problem:** Teams adopting AI repeat the same mistakes: wrong starting point, missing data governance, no evaluation criteria, unclear ownership.

**What it could contain:** A collection of markdown playbooks — not code — covering topics like "Running your first AI POC," "Evaluating LLM output quality," "Designing human-in-the-loop workflows," "Sanitizing workflows for sharing." Each playbook follows: context → steps → checklist → common pitfalls.

**Why it fits the portfolio:** Positions the author as someone who systematizes knowledge — valuable for senior implementation and consulting roles.

---

### Enterprise AI Patterns

**Problem:** Teams rebuilding the same architectural patterns (input → model → output, event-driven enrichment, human-in-the-loop review) without a shared reference.

**What it could contain:** A catalog of reusable AI workflow patterns with diagrams, when-to-use guidance, and links to working examples. Patterns like: "Event-driven enrichment," "Conversational loop," "Batch analysis with review gate," "Multi-system orchestration."

**Why it fits the portfolio:** Shows architectural thinking at the pattern level — not tied to one tool or vendor.

---

### AI Notes and Experiments

**Problem:** Continuous learning in AI requires experimentation, but experiments scattered across tools and notes are hard to reference later.

**What it could contain:** A structured log of AI experiments — model comparisons, prompt iterations, tool evaluations — each with: hypothesis, setup, result, takeaway. Not polished projects; honest lab notes.

**Why it fits the portfolio:** Demonstrates curiosity and continuous learning without overselling incomplete work.

---

## Prioritization guidance

If building incrementally, this order maximizes portfolio impact:

1. **AI Implementation Playbooks** — low code, high credibility, immediately useful
2. **Enterprise AI Patterns** — complements this repository with reusable reference material
3. **Executive Brief Generator** — small, runnable, demonstrates executive communication
4. **Customer Health Agent** — second workflow track, shows breadth across lifecycle stages
5. **AI Discovery Assistant** — meta-tool that frames all other work
6. **AI Notes and Experiments** — ongoing, never "done"

---

## Related documentation

- [Root README](../README.md)
- [Discovery framework](discovery.md)
