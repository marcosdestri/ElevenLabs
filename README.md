# AI Voice Agent Demo

Mini **voice agent**: entrada do usuário → **OpenAI** (resposta) → **ElevenLabs** (voz) → `response.mp3`.

## Como rodar

1. Crie o ambiente e instale dependências:

   ```bash
   cd voice-agent-demo
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Configure as chaves (escolha um):

   - **Arquivo `.env`** (recomendado localmente): copie `.env.example` para `.env` e preencha as chaves.
   - **Ou exporte no terminal:**

     ```bash
     export OPENAI_API_KEY="..."
     export ELEVENLABS_API_KEY="..."
     ```

3. Execute:

   ```bash
   python main.py
   ```

   Digite sua mensagem quando aparecer `User:`.

## Variáveis

| Variável | Obrigatória | Descrição |
|----------|-------------|-----------|
| `OPENAI_API_KEY` | sim | Chave da OpenAI |
| `ELEVENLABS_API_KEY` | sim | Chave da ElevenLabs |
| `OPENAI_MODEL` | não | Padrão: `gpt-4o-mini` |

Não commite `.env` nem chaves no código.
