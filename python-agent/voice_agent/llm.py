"""Response generation: customer text → assistant text."""

from __future__ import annotations

from openai import OpenAI, OpenAIError

from voice_agent import settings


def generate_response(user_message: str, *, client: OpenAI | None = None) -> str:
    """Stage 2 — Response generation: produce assistant text for TTS.

    **Implementation today:** OpenAI Chat Completions. The same function name and
    contract can back any LLM provider (Vertex, Azure OpenAI, Anthropic, etc.) or
    a routing layer—swap the body, keep ``pipeline`` unchanged.

    In production, add retrieval, tools, and policy here. ``client`` is injectable
    for unit tests.
    """
    api_client = client or OpenAI(api_key=settings.openai_api_key())
    model = settings.openai_model()

    # LLM call with a prompt tuned for short, speakable answers
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

    # Normalize text before the voice stage
    text = completion.choices[0].message.content
    if not text or not text.strip():
        raise RuntimeError("OpenAI returned an empty reply.")
    return text.strip()
