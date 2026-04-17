"""Response generation: customer text → assistant text (OpenAI Chat Completions)."""

from __future__ import annotations

from openai import OpenAI, OpenAIError

from voice_agent import settings


def generate_response(user_message: str, *, client: OpenAI | None = None) -> str:
    """Step 2 — Response: produce assistant text suitable for text-to-speech.

    In production this layer gains retrieval, tools, and policy; here it is a
    single Chat Completions call. ``client`` may be injected in tests.
    """
    api_client = client or OpenAI(api_key=settings.openai_api_key())
    model = settings.openai_model()

    # Call the model with a voice-oriented system prompt
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

    # Extract and normalize text for the TTS step
    text = completion.choices[0].message.content
    if not text or not text.strip():
        raise RuntimeError("OpenAI returned an empty reply.")
    return text.strip()
