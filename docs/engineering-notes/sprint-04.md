# Sprint 04 - Provider Factory Pattern

## Sprint Goal

Decouple business logic from specific LLM providers by introducing an extensible provider architecture.

---

## What We Built

- Base provider abstraction
- Gemini provider
- Provider factory
- LLM manager
- Refactored ChatService

Architecture

```
Chat Service

↓

LLM Manager

↓

Provider Factory

↓

Gemini Provider

↓

Gemini SDK
```

---

## Why We Built It

The application should not depend on a single LLM provider.

Adding OpenAI, Claude, or Ollama should require minimal code changes.

---

## Alternatives Considered

### Direct Gemini Usage

```
Chat Service

↓

Gemini
```

Rejected.

Reason:

Tightly coupled architecture.

---

### Factory Pattern

Selected.

Reason:

Supports multiple providers with minimal changes.

---

## Trade-offs

Pros

- Highly extensible
- Easy provider switching
- Clean architecture
- Supports Dependency Inversion

Cons

- More abstraction
- Additional files

---

## Challenges Faced

- Understanding abstractions
- Separating responsibilities
- Designing extensible architecture

---

## Key Learnings

- Factory Pattern
- SOLID principles
- Dependency Inversion
- Separation of Concerns
- Provider abstraction

---

## Interview Takeaways

Question:

Why introduce a Provider Factory?

Answer:

To decouple business logic from vendor-specific SDKs and make the system extensible without modifying existing services.

---

## Next Sprint

Prompt Management Framework.