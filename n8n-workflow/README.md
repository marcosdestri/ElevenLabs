# Sales Call Intelligence Workflow

Sanitized n8n export — event-driven automation that enriches deal board items with AI-generated qualification insight from call transcripts.

For business context, discovery, and impact, start with the [root README](../README.md#track-1--sales-call-intelligence).

---

## What's inside

| File | Description |
|------|-------------|
| `sales-intelligence.json` | 14-node n8n workflow (sanitized — credentials removed) |

---

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

**Will not run out of the box.** Credentials and webhook paths were removed during sanitization.

---

## Documentation

- [Workflow walkthrough](../docs/n8n-sales-intelligence.md)
- [Sample output (fictional)](../docs/examples/sales-agent-output-sample.md)
- [Architecture](../docs/architecture.md)
- [Discovery framework](../docs/discovery.md)
