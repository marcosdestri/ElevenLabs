# Architecture

This document describes the design of both tracks in this repository and the reasoning behind key decisions.

---

## Shared pattern: input → model → output

Both the Python voice agent and the n8n sales intelligence workflow follow the same abstract pipeline:

1. **Capture** — receive input (CLI text, webhook event + data fetch)
2. **Reason** — LLM generates a response or analysis
3. **Deliver** — output to the user (MP3 file, monday.com update)

This separation is intentional. In enterprise deployments, each stage often maps to a different team, vendor, or compliance boundary.

---

## Voice agent architecture

### Sequence diagram

```mermaid
sequenceDiagram
  participant User
  participant CLI as pipeline.py
  participant LLM as llm.py_OpenAI
  participant TTS as tts.py_ElevenLabs
  User->>CLI: text_input
  CLI->>LLM: customer_utterance
  LLM-->>CLI: assistant_reply
  CLI->>TTS: assistant_reply
  TTS-->>CLI: voice_response.mp3
```

### Module responsibilities

| Module | File | Responsibility |
|--------|------|----------------|
| Orchestration | `voice_agent/pipeline.py` | Runs one turn: input → LLM → TTS |
| Input | `pipeline.py` → `read_customer_input()` | CLI text capture (STT placeholder) |
| Reasoning | `voice_agent/llm.py` | OpenAI Chat Completions call |
| Speech | `voice_agent/tts.py` | ElevenLabs REST API → MP3 |
| Config | `voice_agent/settings.py` | Env vars, system prompt, defaults |
| Entry | `voice_agent/cli.py`, `main.py` | CLI with exit codes |

### Design decisions

| Decision | Rationale |
|----------|-----------|
| Text input instead of STT | De-risks the LLM + TTS loop before adding speech recognition complexity |
| Single-turn only | Simplest valid prototype; multi-turn requires memory and state management |
| Injectable OpenAI client in `llm.py` | Enables unit tests without live API calls |
| Separate `llm.py` and `tts.py` | Vendor swap requires changing one module, not the orchestrator |
| `.env` loaded from `python-agent/` root | Runs consistently regardless of shell working directory |

---

## n8n sales intelligence architecture

### Flow diagram

```mermaid
flowchart TD
  Webhook --> GetItem[Get_item_values]
  GetItem --> SplitID[Split_opportunity_ID]
  SplitID --> OppInfo[Get_Opportunity_info]
  OppInfo --> ConvID[Get_last_conversation_ID]
  ConvID --> Validate{Gong_call_exists?}
  Validate -->|No| NoAnalysis[Add_update_without_agent]
  Validate -->|Yes| Transcript[Get_Call_Transcript]
  Transcript --> Concat[concatenate_transcript]
  Concat --> Agent[AI_Agent_MEDDPICC]
  Agent --> Summary[Add_opty_summary_to_item]
```

### High-level overview

```mermaid
flowchart LR
  subgraph trigger [Trigger]
    WH[monday_Webhook]
  end

  subgraph data [Data layer]
    SF[Snowflake]
    CRM[Salesforce_opportunities]
    Gong[Gong_transcripts]
  end

  subgraph ai [AI layer]
    LLM[OpenAI_Chat_Model]
    Agent[AI_Agent]
    Redis[Redis_Memory]
  end

  subgraph output [Output]
    Update[monday_Update]
  end

  WH --> SF
  SF --> CRM
  SF --> Gong
  Gong --> Agent
  LLM --> Agent
  Redis --> Agent
  Agent --> Update
```

### Design decisions

| Decision | Rationale |
|----------|-----------|
| Snowflake as data hub | CRM and Gong data already consolidated in the warehouse — one query layer |
| Branch before AI agent | Avoids running analysis when no Gong call exists |
| Code nodes for ID extraction and transcript formatting | Lightweight transforms without external dependencies |
| Long domain prompt in AI Agent node | Encodes sales methodology (MEDDPICC + Command of the Message) as configuration |
| Redis Chat Memory | n8n LangChain pattern for agent context within a single run |
| Sanitized export in git | Documents the workflow design without exposing credentials or internal paths |

---

## How the two tracks relate

```mermaid
flowchart LR
  subgraph voiceAgent [python-agent]
    Input[TextInput_CLI]
    LLM[OpenAI_Chat]
    TTS[ElevenLabs_TTS]
    MP3[voice_response.mp3]
    Input --> LLM --> TTS --> MP3
  end

  subgraph n8nFlow [n8n-workflow]
    WH[monday_Webhook]
    SF[Snowflake_CRM_Gong]
    Agent[AI_Agent_MEDDPICC]
    Update[monday_Update]
    WH --> SF --> Agent --> Update
  end

  voiceAgent -.->|"same pattern: input → model → output"| n8nFlow
```

The voice agent demonstrates how **spoken delivery** could sit on top of the same intelligence that the n8n workflow produces in text form. In a full enterprise deployment, the n8n analysis could feed a voice channel — but this repository keeps them as independent, runnable demos.

---

## Related documentation

- [Voice agent deep dive](voice-agent.md)
- [n8n workflow walkthrough](n8n-sales-intelligence.md)
- [Root README](../README.md)
