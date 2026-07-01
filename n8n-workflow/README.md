# n8n Sales Intelligence Workflow

Sanitized export of the **Enrich WaitingRoom Latam** workflow — monday.com webhook → Snowflake (Salesforce + Gong) → AI Agent → monday.com update.

## Import

1. Open n8n → **Workflows** → **Import from File**
2. Select `sales-intelligence.json`
3. Configure credentials in the n8n UI:
   - monday.com
   - Snowflake
   - OpenAI
   - Redis
4. Set the webhook path (redacted in the export)
5. Connect to your monday.com integration and activate

**This workflow will not run out of the box.** Credentials and webhook paths were removed during sanitization.

## What's inside

| File | Description |
|------|-------------|
| `sales-intelligence.json` | 14-node n8n workflow (sanitized) |

## Documentation

- [n8n workflow walkthrough](../docs/n8n-sales-intelligence.md)
- [Sample agent output (fictional)](../docs/examples/sales-agent-output-sample.md)
- [Architecture overview](../docs/architecture.md)
- [Root README](../README.md)
