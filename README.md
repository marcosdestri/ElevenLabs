# AI Voice Customer Agent

**A solutions-engineering prototype** of a voice-enabled customer interaction: one turn from **what the customer says** → **what the agent answers** → **how that answer sounds** when spoken aloud.

It is intentionally small—easy to read, demo, and extend—but structured like the **core loop** you would reuse behind STT, telephony, or a web widget in production.

---

## Overview

**What this is:** a runnable spike that shows how **LLM reasoning** and **high-quality TTS** combine into a **voice interface** for customer scenarios—not a generic “text to MP3” script.

**Why it exists:** teams exploring **voice support**, **IVR modernization**, or **AI-assisted contact centers** need a credible vertical slice before buying platforms or wiring CRMs. This repo is that slice in code: clear steps, named outputs, and room to grow without rewriting from scratch.

**Pipeline (one turn):**

1. **Input** — what the customer communicates (typed in the CLI today; speech input later).
2. **Response** — assistant text from **OpenAI** (`generate_response`), tuned for short, speakable answers.
3. **Voice** — spoken audio from **ElevenLabs** (`generate_voice`), saved as **`voice_response.mp3`** at the project root.

---

## Example interaction

| Step | What happens (illustrative) |
|------|------------------------------|
| **Input** | Customer types: *“My order was supposed to arrive yesterday—can you help?”* |
| **Response** | Model returns a concise, empathetic reply (e.g. acknowledges delay, offers next steps). |
| **Voice** | That reply is synthesized to speech; you play **`voice_response.mp3`** locally. |

In a pilot, the same three steps attach to **phone or chat**: STT → LLM (+ tools / KB) → streaming TTS—the architecture stays familiar.

---

## Use cases

- **Customer support** — Tier‑1 FAQs, order status, password resets: **consistent wording** and **voice** reduce load on live agents while keeping tone on-brand.
- **Automation** — Turn events (shipment out, appointment booked) into **spoken** updates for dialers, kiosks, or field apps; the LLM layer personalizes phrasing from structured data.
- **Voice assistants & concierge** — Hotels, banking, retail: natural confirmations and “what happens next” without recording hundreds of static audio clips.

---

## Architecture

- **Input handling** — `read_customer_input()` (CLI); same boundary later receives text from STT.
- **Response generation** — `generate_response()` in `voice_agent/llm.py` (OpenAI Chat Completions).
- **Voice generation** — `generate_voice()` in `voice_agent/tts.py` (ElevenLabs REST → MP3).

**Orchestration** — `voice_agent/pipeline.py` runs the three steps in order. **Configuration** — `voice_agent/settings.py` (env, defaults, `.env` loading). **CLI** — `voice_agent/cli.py` + `main.py` / `python -m voice_agent`.

---

## Why this matters

**Voice is an interface, not a gimmick.** Many customers still **call** or use **hands-free** contexts; reading a wall of text is not always viable. Pairing an LLM with TTS lets you **iterate on wording and tone** quickly while proving integrations to stakeholders.

**Scalable story:** the same separation—**capture utterance → decide → render speech**—maps to queues, session stores, observability, and human handoff as the product matures. This prototype keeps that story **visible in the code**, not buried in one long script.

---

## How to run

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # add OPENAI_API_KEY and ELEVENLABS_API_KEY
python main.py              # or: python -m voice_agent
```

When prompted with `User:`, type a customer message and press Enter. On success you get terminal output plus **`voice_response.mp3`** in the project folder.

**Tests (no live APIs):**

```bash
python -m pytest
```

**Project layout (high level):**

```text
voice_agent/   settings, llm, tts, pipeline, cli
tests/         pytest with mocks
main.py        entry shim
```

---

## Next steps

| Direction | What it unlocks |
|-----------|-----------------|
| **Conversation memory** | Multi-turn context, summarization, and handoff payloads to human agents. |
| **External APIs & tools** | Order lookup, ticketing, calendars—ground responses in **your** systems, not only the model. |
| **Speech input (STT)** | True voice-in / voice-out; swap the input function, keep response + voice modules. |
| **Streaming & latency** | Streamed LLM + streamed TTS for tolerable real-time phone and web UX. |
| **Channels & scale** | WebRTC, SIP, or messaging surfaces; horizontal workers, rate limits, and observability per tenant. |

---

*Prototype only—meant to align engineering, product, and buyers on a **voice AI customer journey** before production hardening.*
