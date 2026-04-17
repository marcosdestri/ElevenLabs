"""ElevenLabs Text-to-Speech — the *voice* step of the pipeline."""

from __future__ import annotations

from pathlib import Path

import requests

from voice_agent import settings


def synthesize_speech_bytes(
    text: str,
    *,
    voice_id: str = settings.DEFAULT_VOICE_ID,
) -> bytes:
    """Call ElevenLabs TTS API; return raw MP3 bytes."""
    url = settings.ELEVENLABS_TTS_URL.format(voice_id=voice_id)
    headers = {
        "xi-api-key": settings.elevenlabs_api_key(),
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    payload = {"text": text, "voice_settings": settings.VOICE_SETTINGS}

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=settings.REQUEST_TIMEOUT_S,
    )
    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        detail = response.text or str(exc)
        raise RuntimeError(
            f"ElevenLabs HTTP {response.status_code}: {detail}"
        ) from exc

    return response.content


def write_mp3(audio: bytes, path: Path) -> Path:
    path.write_bytes(audio)
    return path


def synthesize_voice_file(
    response_text: str,
    output_path: Path | None = None,
) -> Path:
    """Synthesize speech and write MP3 to disk."""
    target = output_path or settings.DEFAULT_OUTPUT
    audio = synthesize_speech_bytes(response_text)
    return write_mp3(audio, target)
