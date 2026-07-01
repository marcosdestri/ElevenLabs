# Sample Sales Agent Output (Fictional)

This is a **fictional, sanitized example** of the kind of analysis the n8n AI Agent produces when a Gong call exists for an opportunity. It illustrates the MEDDPICC + Command of the Message format — not real customer data.

---

## Context (fictional)

- **Opportunity:** Acme Corp — Enterprise Platform Expansion
- **Stage:** Waiting room (new item on monday.com board)
- **Trigger:** Webhook fired when item was created
- **Data sources:** Salesforce opportunity row + latest Gong call transcript (both via Snowflake)

---

## Sample monday.com update (fictional)

```text
Automatic update by n8n

Análise do agente para a Oportunidade Acme Corp — Enterprise Platform Expansion

## Resumo Executivo

Call de discovery com VP de Operações (Maria Silva) e Gerente de TI (Carlos Mendes).
Acme está consolidando ferramentas de gestão de projetos após aquisição de duas
filiais. Pain principal: falta de visibilidade cross-funcional e processos manuais
em planilhas.

## MEDDPICC

### Metrics (M)
- Reduzir tempo de reporting semanal de 8h para 2h (meta declarada pela VP)
- Aumentar taxa de conclusão de projetos de 62% para 85% em 12 meses

### Economic Buyer (E)
- Maria Silva, VP de Operações — aprovadora final confirmada na call
- Budget aprovado para Q3; decisão depende de POC com equipe de TI

### Decision Criteria (D)
- Facilidade de adoção (equipe não-técnica)
- Integração com Salesforce e Slack existentes
- Time-to-value em menos de 30 dias

### Decision Process (D)
- POC de 2 semanas com equipe piloto (15 usuários)
- Avaliação técnica por Carlos Mendes (TI)
- Aprovação final por Maria Silva após POC

### Paper Process (P)
- Contrato anual via procurement; ciclo estimado de 3-4 semanas após aprovação

### Identify Pain (I)
- 3 ferramentas diferentes entre filiais, sem padronização
- Reporting manual consome 1 FTE equivalente por semana
- Baixa visibilidade para liderança sobre status de projetos

### Champion (C)
- Carlos Mendes (Gerente de TI) — engajado, fez perguntas técnicas detalhadas,
  ofereceu-se para liderar o POC

### Competition (C)
- Mencionou avaliação paralela com Asana e Smartsheet
- Diferenciador percebido: flexibilidade de workflows e adoção visual

## Próximos Passos Sugeridos

1. Enviar proposta de POC com escopo de 2 semanas e 15 usuários
2. Agendar sessão técnica com Carlos Mendes para integrações Salesforce/Slack
3. Preparar business case com ROI baseado na redução de 6h/semana de reporting

Gong call: https://app.gong.io/call?id=EXAMPLE-REDACTED
```

---

## When no Gong call exists

If the workflow finds no linked Gong conversation, it posts a short notice instead:

```text
Automatic update by n8n

Não há nenhuma conversa do gong registrada para essa oportunidade
```

No AI analysis runs in this branch.

---

## Related documentation

- [n8n workflow walkthrough](../n8n-sales-intelligence.md)
- [Root README](../../README.md)
