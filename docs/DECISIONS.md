# Architecture Decisions

This document records permanent architectural decisions.

---

## Decision 001

Title

Recommendation Only

Decision

Oklix never executes tasks.

Reason

Execution belongs to caller agents.

Status

Accepted

---

## Decision 002

Title

Provider Agnostic

Decision

Oklix never depends on a specific provider.

Reason

Avoid vendor lock-in.

Status

Accepted

---

## Decision 003

Title

Explainable Decisions

Decision

Every recommendation must include an explanation.

Reason

Increase trust.

Status

Accepted

---

## Decision 004

Title

Adaptive Intelligence

Decision

Provider health and experience influence recommendations.

Reason

Recommendations should improve over time.

Status

Accepted

---

## Decision 005

Title

Metadata Only

Decision

Provider information is metadata.

Oklix does not invoke providers.

Reason

Maintain separation of concerns.

Status

Accepted

---

## Decision 006

Title

Execution Plan

Decision

Execution plans are recommendations only.

They are never executed by Oklix.

Reason

Execution belongs to caller agents.

Status

Accepted

---

## Decision 007

Title

Clean Decision Core

Decision

The Decision Core must remain independent of runtime, orchestration, tools, MCP, and execution frameworks.

Reason

Keep the core simple, testable, and reusable.

Status

Accepted

---

## Decision 008

Title

Single Responsibility

Decision

Oklix owns decision intelligence only.

All operational concerns are delegated to external agents.

Reason

Maintain a clear product identity and long-term architectural stability.

Status

Accepted