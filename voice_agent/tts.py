"""Voice output: assistant text → spoken audio file."""

from __future__ import annotations

from pathlib import Path

import requests

from voice_agent import settings


def _fetch_tts_audio(text: str, *, voice_id: str = settings.DEFAULT_VOICE_ID) -> bytes:
    """HTTP call to the TTS vendor; returns raw MP3 bytes (no file I/O)."""
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


def _write_mp3(audio: bytes, path: Path) -> Path:
    """Write synthesized bytes to disk."""
    path.write_bytes(audio)
    return path


def generate_voice(
    assistant_text: str,
    output_path: Path | None = None,
) -> Path:
    """Stage 3 — Voice output: TTS for ``assistant_text`` → MP3 on disk.

    **Vendor today:** ElevenLabs. Same signature supports another TTS backend
    if enterprise routing or latency requirements change.
    """
    target = output_path or settings.DEFAULT_OUTPUT
    audio_bytes = _fetch_tts_audio(assistant_text)
    return _write_mp3(audio_bytes, target)
