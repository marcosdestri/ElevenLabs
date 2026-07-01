# Discovery Framework

How enterprise AI solutions begin — before architecture, before model selection, before any code is written.

---

## Why discovery comes first

Enterprise organizations do not have a "technology problem." They have operational problems that technology — including AI — may help solve.

The most common failure mode in AI implementation is skipping discovery and starting with tooling: picking a model, choosing a platform, building a demo that answers the wrong question. Discovery prevents that.

---

## The questions that matter

These questions shaped every project in this repository. They apply regardless of industry, company size, or AI maturity.

### Who

- Who performs this task today?
- Who consumes the output?
- Who approves or owns the outcome?
- Who will resist change — and why?

### Where

- Where does the workflow begin? (Trigger moment)
- Where does it end? (Deliverable destination)
- Which systems are already involved?
- Where does data live today — and is it reliable?

### What

- What does the user need to see, hear, or receive to take action?
- What does "done" look like from the user's perspective?
- What happens when expected data is missing?
- What quality bar must the output meet before users will trust it?

### When

- When should automation run? (Event, schedule, on-demand)
- When should a human stay in the loop?
- When is AI the right tool — versus a simpler rule, lookup, or notification?

### Why

- Why does this problem matter to the business?
- Why hasn't it been solved already?
- Why is AI appropriate here specifically?
- Why would users adopt this over their current workaround?

---

## From discovery to design

Discovery answers feed directly into solution design:

| Discovery insight | Design decision |
|-------------------|-----------------|
| Reps start on the deal board | Trigger on board event, deliver output back to the board |
| CRM and call data already in the warehouse | Use Snowflake as integration layer — no new connectors |
| No call recording = no analysis possible | Branch explicitly; post a notice instead of running AI |
| Stakeholders need to *hear* voice output | Build a prototype that produces audible MP3, not API logs |
| Full telephony is months away | Defer STT; validate reasoning + speech output first |

---

## Discovery in practice — two examples

### Sales call intelligence

**Starting observation:** Reps spend 20–30 minutes per deal manually reading Gong transcripts and writing qualification notes on the board.

**Discovery questions:**
- Can we trigger when the deal item is created? → Yes, via webhook
- Is transcript data accessible programmatically? → Yes, via Snowflake
- What format does the rep need? → MEDDPICC-style structured analysis
- What if there's no call yet? → Post a clear notice; do not hallucinate

**Result:** Event-driven workflow that enriches the board item automatically.

### Voice customer agent

**Starting observation:** Leadership wants to explore voice AI but cannot commit to telephony infrastructure without proof the interaction works.

**Discovery questions:**
- What is the minimum loop to validate? → Input → reasoning → spoken output
- What can we defer? → STT, multi-turn, CRM integration, deployment
- Who needs to experience it? → Business stakeholders, not engineers
- How fast can we produce something tangible? → CLI prototype in hours

**Result:** Runnable local demo that produces audible output from a typed customer message.

---

## What discovery is not

- A requirements document that freezes scope before experimentation
- A checklist that replaces conversation with stakeholders
- An excuse to delay building — discovery and prototyping happen together
- A one-time phase — it continues through iteration, feedback, and refinement

---

## Related documentation

- [Root README](../README.md)
- [Architecture](architecture.md)
- [Portfolio roadmap](portfolio-roadmap.md)
