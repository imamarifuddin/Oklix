# Oklix Architecture

Current Architecture

```
Caller Agent
      │
      ▼
 Oklix API
      │
      ▼
 ASP Service
      │
      ▼
 Recommendation Builder
      │
      ├── Analyzer
      ├── Capability Engine
      ├── Cost Engine
      ├── Latency Engine
      ├── Ranking Engine
      ├── Tradeoff Engine
      ├── Explanation Engine
      ├── Provider Knowledge
      ├── Provider Health
      ├── Experience Engine
      └── Recommendation History
      │
      ▼
 Decision Response
      │
      ▼
 Caller Agent Executes
```

---

# Responsibilities

Analyzer

- Understand task

Capability Engine

- Evaluate model capabilities

Cost Engine

- Estimate execution cost

Latency Engine

- Estimate latency

Ranking Engine

- Rank candidate models

Tradeoff Engine

- Compare alternatives

Explanation Engine

- Explain recommendations

Recommendation Builder

- Produce final recommendation

---

# Out of Scope

The following MUST NOT exist inside Oklix.

- AI execution
- Agent execution
- Workflow execution
- Tool execution
- Filesystem execution
- Browser execution
- Web search execution
- MCP runtime
- Multi-agent orchestration
- Provider SDK execution

These responsibilities belong to caller agents.