"""OpenAI Chat Completions — the *response* step of the pipeline."""

from __future__ import annotations

from openai import OpenAI, OpenAIError

from voice_agent import settings


def generate_response(user_message: str, *, client: OpenAI | None = None) -> str:
    """Map customer text to assistant reply (plain text suitable for TTS).

    ``client`` is optional for tests (inject a mock OpenAI client).
    """
    api_client = client or OpenAI(api_key=settings.openai_api_key())
    model = settings.openai_model()

    try:
        completion = api_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": settings.SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
        )
    except OpenAIError as exc:
        raise RuntimeError(f"OpenAI request failed: {exc}") from exc

    text = completion.choices[0].message.content
    if not text or not text.strip():
        raise RuntimeError("OpenAI returned an empty reply.")
    return text.strip()
