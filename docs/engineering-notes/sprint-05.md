# Sprint 05 — Testing Infrastructure & Mocking

## Sprint Goal

Introduce a professional testing infrastructure that allows application logic to be tested without relying on external LLM providers.

---

# What We Built

- Test folder structure
- Fake LLM Provider
- Unit testing with Pytest
- ChatService unit tests
- Offline testing workflow

---

# Why We Built It

External AI providers are:

- Slow
- Rate limited
- Costly
- Non-deterministic

Professional software should not rely on external APIs during unit testing.

---

# Alternatives Considered

### Option 1

Test against Gemini API

Pros

- Real responses

Cons

- Consumes quota
- Slow
- Network dependent

---

### Option 2 (Chosen)

Fake Provider

Pros

- Fast
- Deterministic
- Free
- Reliable

Cons

- Doesn't validate provider integration

---

# Trade-offs

Using FakeProvider means we sacrifice testing the real provider during unit tests.

This is acceptable because provider communication belongs in integration tests.

---

# Interview Takeaways

### Why Fake Providers?

To isolate business logic from external dependencies.

---

### Why Unit Tests?

To verify application behavior quickly and deterministically.

---

### Why Dependency Injection?

Dependency Injection allows swapping real providers with fake implementations during testing without modifying application code.

---

# Deliverables

- FakeProvider
- Pytest
- ChatService tests
- Offline development workflow

---

Sprint Status

✅ Completed