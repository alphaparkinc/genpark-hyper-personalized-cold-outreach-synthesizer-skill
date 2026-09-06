# GenPark AI Agent Skill - Hyper-Personalized Cold Outreach Synthesizer

Automates high-conversion, multi-touch B2B outbound cadences tailored to target firmographics, executive roles, and real-time company catalysts.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[Account Catalysts & Prospect Data] --> B[Personalization Engine]
    B --> C[Touch 1: Contextual Hook & Pain Hypothesis]
    B --> D[Touch 2: Benchmark Metrics & Proof Point]
    B --> E[Touch 3: Graceful Breakup / Loop Closure]
    C --> F[Spam Word Analysis Filter]
    D --> F
    E --> F
    F --> G[Deliverable 3-Touch Outreach Sequence]
```

## Features
- **Dynamic Context Weaving**: Integrates funding milestones, team growth, and role responsibilities seamlessly.
- **Built-In Deliverability & Spam Filter**: Screens output text against common spam triggers to ensure inbox placement.
- **Zero External Dependencies**: Pure Python 3.9+ standard library.
- **Designed for Autonomous SDR Workflows**: Bridges intelligence gathering with automated draft dispatch.
