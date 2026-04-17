# AI Voice Customer Agent

**Demonstrates a scalable, customer-facing voice AI loop**—from what the customer expresses, to a model-generated answer, to spoken audio—so stakeholders can validate the **same integration pattern** that later plugs into STT, CRM, queues, and telephony.

**Together with the n8n workflow in this repo**, the story covers **enterprise orchestration** (monday.com, Snowflake, Gong data, AI) **and** how **voice** can sit on top as another customer-facing channel.

---

## Repository structure

This repository is split into **two** top-level folders—one for the **runnable Python prototype**, one for the **automation definition** you can import into n8n.

| Folder | Contents | Who uses it |
|--------|----------|-------------|
| **`python-agent/`** | `voice_agent/` package, `main.py`, `tests/`, `requirements.txt`, `.env.example`. | Engineers running the **voice CLI** locally or in CI. |
| **`n8n-workflow/`** | `sales-intelligence.json` — sanitized export of the **Enrich WaitingRoom Latam** workflow. | Solutions / ops importing the graph into **n8n** and wiring credentials there. |

At the **root** you also have **`README.md`** (this file), **`LICENSE`**, **`pyproject.toml`** (pytest + ruff scoped to `python-agent/`), and **`.gitignore`**.

**Voice output path:** `python-agent/voice_response.mp3` (created when you run the CLI from `python-agent/`).

---

**Scan this first (≈30s)**

| | |
|--|--|
| **What** | **(1)** One-turn **voice** prototype in `python-agent/`: input → LLM → TTS. **(2)** **`n8n-workflow/sales-intelligence.json`** — monday.com · Snowflake · Gong transcript data · AI agent. |
| **Why** | De-risk **voice + AI** and show **multi-system automation** before heavy platform spend. |
| **Stack** | Python · OpenAI · ElevenLabs · `pytest` · **n8n** (workflow JSON). |

---

## Architecture (Python voice agent)

End-to-end pipeline for **each** customer turn inside `python-agent/`:

```text
User Input  →  Response Generation  →  Voice Output
```

| Stage | Responsibility | Location |
|-------|----------------|----------|
| **User Input** | Capture what the customer said (text today; audio later). | `python-agent/voice_agent/pipeline.py` → `read_customer_input()` |
| **Response Generation** | Turn utterance into assistant text safe to read aloud. | `python-agent/voice_agent/llm.py` → `generate_response()` |
| **Voice Output** | Render that text as speech. | `python-agent/voice_agent/tts.py` → `generate_voice()` → **`voice_response.mp3`** |

**Orchestration:** `run_single_turn()` in `pipeline.py`. **Config:** `settings.py`. **CLI:** `cli.py` or `python main.py` / `python -m voice_agent` **from `python-agent/`.**

---

## Real-world use case: Sales Call Intelligence Automation

**Workflow file:** [`n8n-workflow/sales-intelligence.json`](n8n-workflow/sales-intelligence.json) (sanitized n8n export of *Enrich WaitingRoom Latam*).  
Credentials, webhook paths, and sample payloads were **removed or redacted**; configure secrets in your own n8n instance after import.

### What the workflow does (step by step)

1. **Webhook** — A **monday.com** event (e.g. new item on a sales / “waiting room” board) starts the run; **Respond to Webhook** completes the integration handshake.
2. **Get item values** — Loads the monday pulse so later steps have deal context.
3. **Split opportunity ID** — Code reads the **Salesforce opportunity ID** from the board for Snowflake keys.
4. **Get Opportunity info** — **Snowflake** reads **Salesforce opportunity** rows (`RAW_SALESFORCE_OPPORTUNITIES`).
5. **Get last conversation ID** — Snowflake resolves the latest **Gong-linked** conversation for that opportunity.
6. **Validate if have gong calls on SFDC** — If there is **no** Gong call, **Add update without agent analysis** posts to monday and the branch stops.
7. **Get Call Transcript** — Loads the **Gong transcript** from Snowflake when a call exists.
8. **concatenate the transcript** — Formats transcript blocks into one model-ready string.
9. **AI Agent** (+ **OpenAI Chat Model**, **Redis Chat Memory**) — **Command of the Message® + MEDDPICC** analysis in the transcript’s language.
10. **Add opty summary as update to item** — Writes the analysis to monday, with a **Gong** call link.

### Systems involved

| System | Role |
|--------|------|
| **monday.com** | Trigger + destination for updates. |
| **Snowflake** | Salesforce + Gong transcript data in the warehouse. |
| **Gong** | What was said on the call (via Snowflake tables). |
| **AI agent** | Structured sales intelligence on top of CRM + transcript. |

### Why it matters

- Faster **waiting-room** enrichment without tab-hopping across Salesforce, Gong, and monday.
- **Repeatable** MEDDPICC-style insight at scale.
- **One thread** on the board tied to the opportunity and recording.

### How the two folders connect

- **`n8n-workflow/`** — Shows **multi-system orchestration** as shipped in **n8n** (nodes, branches, connectors).
- **`python-agent/`** — Same **input → model → output** pattern for **spoken** UX; voice is another **surface** on the same intelligence story.

---

## Example interaction (voice agent)

**User input (after `User:`):**

> *“My subscription renewed at the wrong price yesterday—I need this corrected before the next billing cycle.”*

**Assistant response (terminal; illustrative):**

> *“I understand you’re seeing an unexpected renewal price…”*

**Voice output:** ElevenLabs produces **`python-agent/voice_response.mp3`**.

---

## Use cases

- **Customer support** — Tier‑1 answers with **spoken** self-serve.
- **Automation** — Event-driven spoken updates with natural phrasing.
- **Voice assistants** — One spine for LLM + voice vendors.

---

## Why this shape (solutions view)

**Voice is a product surface.** This repo keeps **capture**, **reasoning**, and **speech output** in separate steps—what you need for observability, compliance, and handoff at scale—whether the middle box is this Python agent or an n8n AI node.

---

## How to run

**Voice agent** (from repo root):

```bash
cd python-agent
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # add OPENAI_API_KEY and ELEVENLABS_API_KEY
python main.py         # or: python -m voice_agent
```

**Tests** (from **repository root**, uses root `pyproject.toml`):

```bash
python -m pytest
```

**n8n workflow:** import `n8n-workflow/sales-intelligence.json` in n8n, then attach Monday, Snowflake, OpenAI, and Redis credentials in the UI.

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
