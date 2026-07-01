# Python Voice Agent

Single-turn CLI prototype: text input → OpenAI → ElevenLabs TTS → `voice_response.mp3`.

## Quick start

```bash
cd python-agent
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add OPENAI_API_KEY and ELEVENLABS_API_KEY
python main.py
```

## Environment variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | OpenAI API key |
| `ELEVENLABS_API_KEY` | Yes | ElevenLabs API key |
| `OPENAI_MODEL` | No | Defaults to `gpt-4o-mini` |

## Tests

From repository root:

```bash
python -m pytest
```

## Documentation

- [Voice agent deep dive](../docs/voice-agent.md)
- [Architecture overview](../docs/architecture.md)
- [Root README](../README.md)
