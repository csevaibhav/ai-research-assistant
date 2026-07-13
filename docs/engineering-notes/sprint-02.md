# Sprint 02 - First LLM Integration

## Sprint Goal

Integrate the backend with an LLM while maintaining clean software architecture.

---

## What We Built

- Chat API
- Request model
- Response model
- Chat service
- LLM integration
- Swagger testing

Architecture

```
Client
    │
FastAPI
    │
Chat Service
    │
LLM
```

---

## Why We Built It

Instead of calling the LLM directly from the API layer, we introduced a dedicated service layer.

This separates HTTP concerns from business logic.

---

## Alternatives Considered

### Direct API Calls

```
Endpoint

↓

OpenAI
```

Rejected.

Reason:

Business logic becomes tightly coupled to API endpoints.

---

### Service Layer

```
Endpoint

↓

Service

↓

LLM
```

Selected.

Reason:

Improves maintainability and testing.

---

## Trade-offs

Pros

- Cleaner architecture
- Easier testing
- Easier provider replacement

Cons

- Slightly more files
- Additional abstraction

---

## Challenges Faced

- API authentication
- SDK usage
- Request validation

---

## Key Learnings

- Pydantic models
- FastAPI routers
- Service layer architecture
- LLM API communication

---

## Interview Takeaways

Question:

Why create a ChatService?

Answer:

To isolate business logic from transport logic and allow future provider replacement.

---

## Next Sprint

Production configuration and logging.