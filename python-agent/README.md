# Voice Customer Agent

Runnable prototype that validates the **input → AI reasoning → spoken output** loop.

For business context, discovery, and impact, start with the [root README](../README.md#track-2--voice-customer-agent).

---

## Quick start

```bash
cd python-agent
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add OPENAI_API_KEY and ELEVENLABS_API_KEY
python main.py
```

Type a message after `User:`. The reply prints to the terminal and an MP3 is saved to `voice_response.mp3`.

---

## What this folder contains

| Path | Purpose |
|------|---------|
| `voice_agent/pipeline.py` | Orchestrates one customer turn |
| `voice_agent/llm.py` | OpenAI response generation |
| `voice_agent/tts.py` | ElevenLabs text-to-speech |
| `voice_agent/settings.py` | Configuration and system prompt |
| `tests/` | Unit tests (mocked APIs) |
| `.env.example` | Required environment variables |

---

## Environment variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | OpenAI API key |
| `ELEVENLABS_API_KEY` | Yes | ElevenLabs API key |
| `OPENAI_MODEL` | No | Defaults to `gpt-4o-mini` |

---

## Tests

From repository root:

```bash
python -m pytest
```

---

## Documentation

- [Voice agent deep dive](../docs/voice-agent.md)
- [Architecture](../docs/architecture.md)
- [Discovery framework](../docs/discovery.md)
