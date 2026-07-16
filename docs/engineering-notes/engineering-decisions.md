# Engineering Decisions

This document records the major architectural decisions made during the development of the **AI Research Assistant**.
Architecture Decision Record (ADR).

The objective is not only to document *what* decisions were made, but also *why* they were made, what alternatives were considered, and what trade-offs were accepted.

---

# ADR-001

## Why FastAPI instead of Flask?

### Decision

Use **FastAPI** as the backend framework.

---

### Context

The AI Research Assistant is an API-first application.

It needs:

- High performance
- Automatic API documentation
- Request validation
- Async support
- Clean developer experience

---

### Alternatives Considered

### Flask

Pros

- Mature ecosystem
- Extremely flexible
- Large community

Cons

- Manual validation
- No built-in API documentation
- Requires additional libraries for typing and validation

---

### Django

Pros

- Batteries included
- Authentication
- ORM
- Admin panel

Cons

- Heavy for an API-first AI service
- More components than required

---

### FastAPI ✅

Pros

- Excellent performance
- Automatic Swagger documentation
- Pydantic validation
- Native async support
- Excellent typing support
- Widely adopted for AI services

Cons

- Smaller ecosystem compared to Flask
- Slightly steeper learning curve

---

### Why We Chose It

Most modern AI platforms expose REST APIs.

FastAPI provides excellent performance while reducing boilerplate code.

It also integrates naturally with Python type hints and Pydantic.

---

### Future Considerations

If gRPC or WebSockets become necessary, FastAPI supports both.

---

### Interview Answer

"I selected FastAPI because it provides automatic request validation, interactive API documentation, asynchronous support, and high performance, making it an excellent choice for AI backend services."

---

# ADR-002

## Why Gemini First instead of OpenAI?

### Decision

Use **Google Gemini** during development.

---

### Context

This project is intended for learning and experimentation.

LLM usage will be frequent during development.

---

### Alternatives Considered

### OpenAI

Pros

- Industry standard
- Excellent documentation
- Strong ecosystem

Cons

- Requires API billing
- Development costs accumulate quickly

---

### Gemini ✅

Pros

- Generous free tier
- Strong reasoning capabilities
- Easy API integration
- Good documentation

Cons

- Model names evolve over time
- Different SDK compared to OpenAI

---

### Why We Chose It

Gemini enables rapid experimentation without introducing API costs during development.

Because our architecture is provider-agnostic, switching to OpenAI later requires minimal effort.

---

### Future Considerations

The application will support multiple providers using a common abstraction.

---

### Interview Answer

"We selected Gemini for development due to its generous free tier while designing the application so that the underlying provider can be replaced without changing business logic."

---

# ADR-003

## Why Use the Factory Pattern?

### Decision

Introduce a Provider Factory for LLM selection.

---

### Context

Initially the project supported only Gemini.

Future providers include:

- OpenAI
- Claude
- Ollama
- Azure OpenAI

---

### Alternatives Considered

### Direct SDK Usage

```
ChatService

↓

Gemini SDK
```

Cons

- Tight coupling
- Difficult to replace providers
- Violates Open/Closed Principle

---

### Factory Pattern ✅

```
ChatService

↓

Provider Factory

↓

Provider
```

Pros

- Easy provider switching
- Extensible
- Cleaner architecture

Cons

- Additional abstraction
- More files

---

### Why We Chose It

The Factory Pattern centralizes provider creation and isolates vendor-specific logic.

---

### Future Considerations

Eventually the factory may support dependency injection and provider registration.

---

### Interview Answer

"The Factory Pattern allows the application to support multiple LLM providers while keeping business logic independent from vendor-specific SDKs."

---

# ADR-004

## Why Introduce a Service Layer?

### Decision

Place business logic inside dedicated services.

---

### Context

API endpoints should focus only on HTTP communication.

Business logic belongs elsewhere.

---

### Alternatives Considered

### Endpoint calls SDK directly

```
Endpoint

↓

Gemini
```

Cons

- Difficult testing
- Tight coupling
- Poor maintainability

---

### Service Layer ✅

```
Endpoint

↓

Service

↓

LLM
```

Pros

- Easier testing
- Better organization
- Separation of concerns

---

### Why We Chose It

The service layer isolates application logic from transport logic.

---

### Future Considerations

The same services can later be reused by CLI tools, background jobs, or scheduled tasks.

---

### Interview Answer

"I introduced a service layer to separate HTTP concerns from business logic, making the application easier to test and maintain."

---

# ADR-005

## Why LangGraph instead of CrewAI?

### Decision

Use **LangGraph** as the primary agent orchestration framework.

---

### Context

The project will evolve into a production-grade Agentic AI system.

It requires:

- Stateful workflows
- Human-in-the-loop
- Conditional routing
- Interrupts
- Durable execution

---

### Alternatives Considered

### CrewAI

Pros

- Easy to learn
- Good for demonstrations
- Fast prototyping

Cons

- Less control over execution flow
- Higher-level abstractions
- Limited workflow customization

---

### LangGraph ✅

Pros

- Stateful execution
- Explicit graph modeling
- Conditional routing
- Durable workflows
- Production focused

Cons

- Higher learning curve
- More implementation effort

---

### Why We Chose It

LangGraph provides explicit workflow control, making it better suited for production AI systems.

---

### Future Considerations

CrewAI may still be explored for rapid prototyping and comparison.

---

### Interview Answer

"I selected LangGraph because it provides explicit state management and workflow orchestration, which are essential for building production-grade AI agents."

---

# ADR-006

## Why Redis for Memory?

### Decision

Use Redis for conversational memory.

---

### Context

Agents need fast access to recent conversations.

Memory operations occur frequently.

---

### Alternatives Considered

### PostgreSQL

Pros

- Persistent
- Reliable

Cons

- Higher latency
- Not optimized for session memory

---

### In-memory Python Objects

Pros

- Simple

Cons

- Lost on restart
- Doesn't scale

---

### Redis ✅

Pros

- Extremely fast
- TTL support
- Session storage
- Widely adopted

Cons

- Additional infrastructure

---

### Why We Chose It

Redis provides low-latency storage for conversational state while supporting expiration policies.

---

### Future Considerations

Long-term memory will eventually move to persistent storage.

---

### Interview Answer

"Redis is optimized for low-latency access and session-based data, making it ideal for conversational memory."

---

# ADR-007

## Why ChromaDB for RAG?

### Decision

Use ChromaDB as the initial vector database.

---

### Context

The project requires semantic search over uploaded documents.

---

### Alternatives Considered

### Pinecone

Pros

- Managed service
- Excellent scalability

Cons

- Paid service
- External dependency

---

### Weaviate

Pros

- Powerful
- Flexible

Cons

- More operational complexity

---

### ChromaDB ✅

Pros

- Open source
- Lightweight
- Local development
- Easy integration

Cons

- Less suitable for very large production workloads

---

### Why We Chose It

ChromaDB allows rapid local development while introducing core vector database concepts.

---

### Future Considerations

The abstraction layer will allow migration to Pinecone or Weaviate if production requirements change.

---

### Interview Answer

"I selected ChromaDB because it is lightweight, open source, and ideal for learning and developing Retrieval-Augmented Generation systems locally."

---

# Engineering Principles Followed

Throughout this project, the following principles guide architectural decisions:

- Clean Architecture
- SOLID Principles
- Separation of Concerns
- Dependency Inversion
- Configuration over Hardcoding
- Composition over Inheritance
- Production Readiness over Rapid Prototyping
- Testability
- Maintainability
- Extensibility

---

# Project Philosophy

This project is intentionally being built as if it were a real production system rather than a tutorial.

Every architectural decision prioritizes long-term maintainability, scalability, and engineering quality over the shortest implementation path.

---

# Why FakeProvider Instead of Calling Gemini During Tests?

## Decision

We introduced a FakeProvider implementing the BaseLLMProvider interface.

## Why?

- Eliminates dependency on internet connectivity.
- Prevents API quota exhaustion.
- Makes unit tests deterministic.
- Speeds up development.

## Alternatives

Use the real Gemini API.

## Trade-off

Provider communication is validated only during integration testing, not unit testing.

## Result

Developers can run the entire test suite offline in seconds.