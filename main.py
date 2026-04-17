"""Demo: entrada do usuário → OpenAI → ElevenLabs TTS → MP3."""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
import requests
from openai import OpenAI, OpenAIError

# Carrega .env ao lado deste arquivo (não depende do cwd do terminal)
load_dotenv(Path(__file__).resolve().parent / ".env")

ELEVENLABS_TTS_URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
DEFAULT_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
DEFAULT_OUTPUT = Path("response.mp3")
REQUEST_TIMEOUT_S = 60

DEFAULT_OPENAI_MODEL = "gpt-4o-mini"
VOICE_ASSISTANT_SYSTEM = (
    "You are a helpful voice assistant. Reply in clear, natural language suitable "
    "to be read aloud. Keep answers concise unless the user asks for detail."
)


def _elevenlabs_api_key() -> str:
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "ELEVENLABS_API_KEY está vazia ou ausente. No arquivo .env (pasta do "
            "projeto), use uma linha sem espaços ao redor do =, por exemplo: "
            "ELEVENLABS_API_KEY=sua_chave_aqui — ou exporte a variável no terminal."
        )
    return key


def _openai_api_key() -> str:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "OPENAI_API_KEY está vazia ou ausente. No arquivo .env (pasta do "
            "projeto), use uma linha sem espaços ao redor do =, por exemplo: "
            "OPENAI_API_KEY=sk-... — ou exporte a variável no terminal."
        )
    return key


def generate_ai_reply(user_message: str) -> str:
    """Gera resposta com Chat Completions da OpenAI."""
    model = (os.environ.get("OPENAI_MODEL") or DEFAULT_OPENAI_MODEL).strip()
    client = OpenAI(api_key=_openai_api_key())

    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": VOICE_ASSISTANT_SYSTEM},
                {"role": "user", "content": user_message},
            ],
        )
    except OpenAIError as exc:
        raise RuntimeError(f"Falha na API OpenAI: {exc}") from exc

    content = completion.choices[0].message.content
    if not content or not content.strip():
        raise RuntimeError("A OpenAI devolveu uma resposta vazia.")
    return content.strip()


def synthesize_to_file(
    text: str,
    *,
    voice_id: str = DEFAULT_VOICE_ID,
    output_path: Path = DEFAULT_OUTPUT,
) -> Path:
    """Gera áudio a partir de `text` e grava em `output_path`."""
    url = ELEVENLABS_TTS_URL.format(voice_id=voice_id)
    headers = {
        "xi-api-key": _elevenlabs_api_key(),
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    payload = {"text": text, "voice_settings": VOICE_SETTINGS}

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=REQUEST_TIMEOUT_S,
    )
    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        detail = response.text or str(exc)
        raise RuntimeError(
            f"ElevenLabs retornou {response.status_code}: {detail}"
        ) from exc

    output_path.write_bytes(response.content)
    return output_path


def main() -> None:
    user_input = input("User: ")
    try:
        ai_response = generate_ai_reply(user_input)
    except RuntimeError as err:
        print(err, file=sys.stderr)
        sys.exit(1)

    print("AI:", ai_response)

    try:
        path = synthesize_to_file(ai_response)
    except (RuntimeError, OSError) as err:
        print(err, file=sys.stderr)
        sys.exit(1)

    print(f"Áudio salvo em: {path.resolve()}")


if __name__ == "__main__":
    main()
