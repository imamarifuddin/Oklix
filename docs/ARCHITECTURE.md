# Architecture

## High Level

User

↓

Decision Engine

↓

Analyzer

↓

Capability Engine

↓

Scoring Engine

↓

Ranking Engine

↓

Optimizer

↓

Recommendation

---

## Module Responsibilities

Analyzer

Input

TaskRequest

Output

TaskProfile

Responsibility

- token estimation
- task complexity
- task size

---

Registry

Load seluruh konfigurasi model AI
dari YAML.

---

Capability Engine

Memeriksa:

- vision

- reasoning

- json mode

- streaming

- function calling

- context window

---

Scoring Engine

Menghasilkan skor numerik.

Quality

Cost

Latency

Capability

Strength

↓

Score

---

Ranking Engine

Mengurutkan model
berdasarkan score.

---

Optimizer

Menghasilkan Recommendation.

---

Decision Engine

Pipeline utama.

Input

↓

Analyzer

↓

Ranking

↓

Optimizer

↓

Recommendation