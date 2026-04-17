# AI Voice Customer Agent

**Demonstrates a scalable, customer-facing voice AI loop**—from what the customer expresses, to a model-generated answer, to spoken audio—so stakeholders can validate the **same integration pattern** that later plugs into STT, CRM, queues, and telephony.

---

**Scan this first (≈30s)**

| | |
|--|--|
| **What** | One-turn **voice support** prototype: typed input today; **LLM** + **TTS** out of the box. |
| **Why** | De-risk **voice + AI** for support, IVR refresh, and automation **before** platform spend. |
| **Stack** | Python · OpenAI Chat Completions · ElevenLabs · `pytest` (mocked APIs). |

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
