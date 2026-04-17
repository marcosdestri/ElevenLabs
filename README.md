# AI Voice Customer Agent

**Demonstrates a scalable, customer-facing voice AI loop**—from what the customer expresses, to a model-generated answer, to spoken audio—so stakeholders can validate the **same integration pattern** that later plugs into STT, CRM, queues, and telephony.

**Together with the section below**, this project also tells an **enterprise orchestration** story: connecting sales data, call transcripts, and AI to update systems automatically—plus how **voice** fits as another channel on top of that intelligence.

---

**Scan this first (≈30s)**

| | |
|--|--|
| **What** | **(1)** One-turn **voice** prototype: input → LLM → TTS → `voice_response.mp3`. **(2)** Sanitized **n8n** export: `docs/workflows/sales-intelligence.json` (monday.com · Snowflake · Gong data · AI). |
| **Why** | De-risk **voice + AI** and show **multi-system automation** before heavy platform spend. |
| **Stack** | Python · OpenAI · ElevenLabs · `pytest` · workflow pattern alignable with **n8n** (or similar). |

**Output file:** `voice_response.mp3` (project root).

---

## Architecture

End-to-end pipeline for **each** customer turn:

```text
User Input  →  Response Generation  →  Voice Output
```

| Stage | Responsibility | In this repo |
|-------|----------------|--------------|
| **User Input** | Capture what the customer said (text today; audio later). | `read_customer_input()` in `voice_agent/pipeline.py` |
| **Response Generation** | Turn utterance into assistant text safe to read aloud. | `generate_response()` in `voice_agent/llm.py` |
| **Voice Output** | Render that text as speech customers can hear. | `generate_voice()` in `voice_agent/tts.py` → **`voice_response.mp3`** |

**Orchestration:** `run_single_turn()` in `voice_agent/pipeline.py` runs the three stages in order. **Config:** `voice_agent/settings.py`. **CLI:** `voice_agent/cli.py` or `python main.py` / `python -m voice_agent`.

---

## Real-world use case: Sales Call Intelligence Automation

**Workflow in this repo:** a **sanitized n8n export** of *Enrich WaitingRoom Latam* lives at  
[`docs/workflows/sales-intelligence.json`](docs/workflows/sales-intelligence.json).  
Credentials, webhook paths, and sample payloads were **removed or redacted** so the file is safe to share; re-bind secrets inside your own n8n instance.

### What the workflow does (step by step)

1. **Webhook** — A **monday.com** event (e.g. new item in a sales / “waiting room” board) starts the run; **Respond to Webhook** answers the integration handshake.
2. **Get item values** — Pulls the pulse from monday so downstream steps know the deal context.
3. **Split opportunity ID** — Code reads the **Salesforce opportunity ID** from the board (so Snowflake queries are keyed correctly).
4. **Get Opportunity info** — **Snowflake** reads **Salesforce opportunity** data from the warehouse (`RAW_SALESFORCE_OPPORTUNITIES`).
5. **Get last conversation ID** — Snowflake joins to the latest **Gong-linked** conversation for that opportunity.
6. **Validate if have gong calls on SFDC** — If there is **no** Gong call on record, the flow posts **Add update without agent analysis** on monday and stops—so the board never looks “silent” without explanation.
7. **Get Call Transcript** — When a call exists, Snowflake loads the **Gong transcript** for that conversation.
8. **concatenate the transcript** — Code turns the raw transcript blocks into one clean string for the model.
9. **AI Agent** (+ **OpenAI Chat Model**, **Redis Chat Memory**) — Runs a **Command of the Message® + MEDDPICC** style prompt: MEDDPICC gaps, value conversation, SE attack plan, trap-setting questions—**in the same language as the transcript**.
10. **Add opty summary as update to item** — Writes the analysis back to the **monday** item, including a link to the **Gong** call—so the team sees insight **where they already work**.

### Systems involved

| System | Role in this workflow |
|--------|------------------------|
| **monday.com** | **Trigger + destination**: board events in, structured updates out. |
| **Snowflake** | **Data hub**: Salesforce opportunities, Gong conversation IDs, and **call transcripts** (no separate “Gong API” node—the data is already modeled in the warehouse). |
| **Gong** | **Content**: what was actually said on the call (via transcript tables in Snowflake). |
| **AI agent (OpenAI in n8n)** | **Reasoning layer**: MEDDPICC / value framing on top of CRM + transcript context. |

### Why this matters for the business

- **Waiting-room deals move faster** — New requests get **automatic enrichment** instead of waiting for a human to open Salesforce, Gong, and monday in three tabs.
- **Coaching at scale** — MEDDPICC-style output is **repeatable** across many calls, not only when a director has time to listen.
- **Single source of truth on the board** — Reps and leadership see **one update thread** tied to the opportunity and the call recording.

### How this repo fits

- **`docs/workflows/sales-intelligence.json`** — Shows **multi-system orchestration** the way a Solutions Engineer ships it in **n8n** (nodes, branches, enterprise connectors).
- **`voice_agent/`** — Same **input → model → output** discipline for **spoken** customer experiences (`voice_response.mp3`); voice becomes another **surface** on top of the same intelligence stack.

---

## Example interaction

**User input (typed after `User:`):**

> *“My subscription renewed at the wrong price yesterday—I need this corrected before the next billing cycle.”*

**Assistant response (printed in terminal; illustrative):**

> *“I understand you’re seeing an unexpected renewal price. Here’s what I can do: confirm the plan on your account, explain the charge you’re seeing, and outline how to request a billing review. Would you like me to start with your current plan name?”*

**Voice output:** the same assistant text is sent to **ElevenLabs TTS**; you listen to **`voice_response.mp3`**.

*In production, only the **input surface** changes (phone, app, kiosk); the middle and last stages stay the same shape.*

---

## Use cases

- **Customer support** — Tier‑1 answers, order and billing questions, **spoken** self-serve that feels guided, not robotic.
- **Automation** — Event-driven spoken updates (shipments, appointments) with **natural phrasing** instead of fixed recordings.
- **Voice assistants** — Concierge, banking, retail: **one integration spine** for LLM + voice vendors.

---

## Why this shape (solutions view)

**Voice is a product surface.** Many users still **call** or are **hands-free**; blocks of text are not always the right UX. This repo shows how **decisioning (LLM)** and **delivery (TTS)** stay **decoupled** from **capture (input)**—the same split you need for observability, compliance, and human handoff at scale.

**Not over-built on purpose:** small codebase, clear files, so a hiring manager or buyer sees **systems thinking** (boundaries, naming, test hooks) without wading through frameworks.

---

## How to run

```bash
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # set OPENAI_API_KEY and ELEVENLABS_API_KEY
python main.py         # or: python -m voice_agent
```

```bash
python -m pytest       # fast; no real API calls
```

---

## Next steps

| Track | Outcome |
|-------|---------|
| **Memory & APIs** | Multi-turn context; tools for orders, tickets, calendars. |
| **Speech in** | STT at the input boundary; keep response + voice modules. |
| **Streaming & channels** | Low-latency streams; WebRTC / SIP / messaging. |
| **Scale & ops** | Per-tenant config, rate limits, tracing, cost per turn. |

---

*Prototype for alignment and technical spikes—not production-hardened software.*
