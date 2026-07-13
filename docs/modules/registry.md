# Registry Module

## Responsibility

Registry bertanggung jawab
memuat seluruh informasi model AI
dari registry/models.yaml.

Registry adalah satu-satunya sumber data model.

---

## Input

models.yaml

---

## Output

ModelCapability

---

## Public API

ModelRegistry

get(name)

exists(name)

names()

all()

---

## Dependency

PyYAML

ModelCapability

---

## Used By

Capability Engine

Scoring Engine

Ranking Engine

Optimizer

Decision Engine

---

## Status

Refactoring