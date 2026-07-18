# Sprint 06.1 — PromptContext Architecture

## Sprint Goal

Refactor the prompt framework to replace primitive method parameters with a structured `PromptContext` object.

The objective was to make the prompt pipeline scalable for future AI capabilities such as Retrieval-Augmented Generation (RAG), conversation memory, tool calling, and multi-agent workflows.

---

# What We Built

During this sprint, we introduced a new architectural layer called **PromptContext**.

### Components Added

- PromptContext model
- PromptContext package
- Refactored ResearchPrompt
- Refactored PromptManager
- New PromptManager unit tests

### Updated Architecture

```text
ChatService
      │
      ▼
PromptManager
      │
      ▼
PromptContext
      │
      ▼
PromptRegistry
      │
      ▼
ResearchPrompt
```

The PromptManager is now responsible for constructing the PromptContext object before passing it to prompt templates.

---

# Why We Built It

Initially, prompt templates accepted only a single string:

```python
ResearchPrompt.build(question)
```

While sufficient for simple prompts, this approach would become difficult to maintain as the application grows.

Future AI workflows require considerably more information than just the user's question, including:

- Conversation history
- Retrieved RAG documents
- Tool execution results
- Memory
- User preferences
- Agent state
- System instructions

Passing all of these as individual parameters would lead to long and difficult-to-maintain method signatures.

To solve this, we introduced a single object (`PromptContext`) that encapsulates all prompt-related information.

---

# Architecture Before

```text
ChatService
      │
      ▼
PromptManager
      │
      ▼
ResearchPrompt(question)
```

---

# Architecture After

```text
ChatService
      │
      ▼
PromptManager
      │
      ▼
PromptContext
      │
      ▼
PromptRegistry
      │
      ▼
ResearchPrompt
```

This architecture is significantly more extensible and prepares the project for advanced AI workflows.

---

# Design Pattern Used

## Parameter Object Pattern

Instead of passing multiple primitive parameters,

```python
build(question, history, documents, memory)
```

we now pass a single object,

```python
build(context)
```

Benefits:

- Cleaner interfaces
- Easier extensibility
- Better readability
- Reduced coupling
- Centralized validation

---

# Alternatives Considered

## Option 1 — Multiple Parameters

Example:

```python
build(
    question,
    history,
    documents,
    tool_results
)
```

### Pros

- Simple implementation

### Cons

- Difficult to maintain
- Large method signatures
- Frequent breaking changes
- High coupling

---

## Option 2 — Dictionary

Example:

```python
build({
    "question": "...",
    "history": [...]
})
```

### Pros

- Flexible

### Cons

- No type safety
- No validation
- Weak IDE support
- Easy to introduce bugs

---

## Option 3 — PromptContext (Chosen)

Example:

```python
PromptContext(
    question=...,
    history=[],
    documents=[]
)
```

### Pros

- Type-safe
- Validated with Pydantic
- Easy to extend
- Excellent IDE support
- Clean architecture

### Cons

- Slightly more initial code

---

# Trade-offs

Introducing PromptContext increased the number of classes in the project.

However, this additional abstraction greatly improves maintainability and significantly reduces future refactoring effort.

The trade-off favors long-term scalability over short-term simplicity.

---

# Testing Performed

Unit tests were updated to validate the new prompt pipeline.

The following tests successfully passed:

- FakeProvider tests
- ChatService tests
- PromptManager tests

Test Result:

```
3 passed
```

The prompt framework now works completely offline without requiring Gemini API access.

---

# Challenges Encountered

### Duplicate Prompt Implementation

During refactoring, two different versions of `research_prompt.py` existed in the project.

This caused inconsistent behavior during testing and made debugging confusing.

The issue was resolved by:

- locating duplicate files,
- removing the obsolete implementation,
- keeping a single source of truth inside the `templates` package.

---

### Unit Test Failure

PromptManager tests initially failed because assertions depended on exact prompt wording.

The tests were improved by verifying important semantic content rather than exact formatting, making them more maintainable.

---

# Lessons Learned

This sprint reinforced several important engineering principles:

- Refactor incrementally instead of rewriting large sections at once.
- Maintain only one implementation of each component.
- Write automated tests before introducing additional complexity.
- Encapsulate related data inside dedicated models.
- Use abstractions that support future scalability.

---

# Interview Takeaways

### Why introduce PromptContext?

PromptContext centralizes all information required to construct AI prompts into a single object.

This reduces method complexity and allows the prompt framework to evolve without changing public interfaces.

---

### Why use Pydantic?

Pydantic provides:

- validation
- serialization
- type safety
- IDE support
- FastAPI compatibility

making it an excellent choice for structured prompt models.

---

### Which design pattern was used?

Parameter Object Pattern.

Instead of passing many primitive values, a dedicated object carries all related information.

---

### Which SOLID principle is demonstrated?

Single Responsibility Principle.

Each component has one responsibility:

- ChatService → business logic
- PromptManager → prompt construction
- PromptRegistry → prompt lookup
- PromptTemplate → prompt formatting
- PromptContext → prompt data

---

# Sprint Deliverables

✅ PromptContext model

✅ PromptManager refactoring

✅ ResearchPrompt refactoring

✅ Updated Prompt Framework

✅ Unit tests

✅ All tests passing

---

# Sprint Status

**Completed ✅**

---

# Next Sprint

Sprint 06.2 — Multiple Prompt Templates

Upcoming work includes:

- Summary Prompt
- Question & Answer Prompt
- Code Review Prompt
- Prompt Registry Expansion
- Prompt Metadata