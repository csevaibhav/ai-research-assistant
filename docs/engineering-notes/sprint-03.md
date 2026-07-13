# Sprint 03 - Production Configuration

## Sprint Goal

Refactor the application into a production-ready backend using centralized configuration and logging.

---

## What We Built

- Centralized configuration
- Environment variables
- Logging
- Gemini integration
- Configuration management
- Reusable LLM client

Architecture

```
Configuration

↓

LLM Client

↓

Service
```

---

## Why We Built It

Hardcoding configuration creates maintenance problems.

Centralizing configuration allows easy environment management and improves code quality.

---

## Alternatives Considered

### os.getenv() everywhere

Rejected.

Reason:

Configuration becomes scattered throughout the codebase.

---

### Pydantic Settings

Selected.

Reason:

Type-safe configuration with validation.

---

## Trade-offs

Pros

- Single source of truth
- Easier deployment
- Better testing

Cons

- Slight learning curve

---

## Challenges Faced

- Invalid OpenAI API key
- Migrating to Gemini
- Gemini model availability
- Debugging configuration
- Reading stack traces

---

## Key Learnings

- Environment variables
- Logging
- Configuration management
- Gemini SDK
- API debugging
- Reading stack traces

---

## Interview Takeaways

Question:

Why use Pydantic Settings?

Answer:

To centralize application configuration, improve maintainability, and validate required settings.

---

## Next Sprint

Provider abstraction using Factory Pattern.