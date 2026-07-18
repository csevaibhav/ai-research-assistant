# Sprint 06.2 — Multiple Prompt Templates

## Sprint Goal

Extend the Prompt Framework to support multiple AI capabilities by introducing reusable prompt templates and a centralized Prompt Registry.

The objective was to transform the prompt system from handling a single research prompt into a scalable framework capable of supporting multiple AI tasks without modifying business logic.

---

# What We Built

During this sprint, we expanded the Prompt Framework by introducing multiple prompt templates and registering them through a centralized Prompt Registry.

### Components Added

- SummaryPrompt
- QAPrompt
- CodeReviewPrompt
- Extended PromptRegistry
- Prompt Registry unit tests

### Updated Prompt Framework

```text
PromptManager
      │
      ▼
PromptContext
      │
      ▼
PromptRegistry
      │
      ├── ResearchPrompt
      ├── SummaryPrompt
      ├── QAPrompt
      └── CodeReviewPrompt
```

The Prompt Registry now acts as the single source of truth for discovering available prompt templates.

---

# Why We Built It

Initially, the project supported only one prompt template:

```python
PromptRegistry.get_prompt("research")
```

Although functional, this approach was not sufficient for a production Agentic AI system.

Real-world AI applications perform many different tasks, including:

- Research
- Question Answering
- Summarization
- Code Review
- Planning
- Tool Selection
- Retrieval-Augmented Generation (RAG)

Instead of embedding prompt-selection logic inside business services, we introduced a Prompt Registry capable of managing multiple prompt implementations.

---

# Architecture Before

```text
PromptRegistry
      │
      ▼
ResearchPrompt
```

Only one prompt template existed.

---

# Architecture After

```text
PromptRegistry
      │
      ├── ResearchPrompt
      ├── SummaryPrompt
      ├── QAPrompt
      └── CodeReviewPrompt
```

Adding new prompt types now requires only:

1. Create a prompt template.
2. Register it.

No changes are required in ChatService or PromptManager.

---

# Design Pattern Used

## Registry Pattern

Instead of selecting prompt templates using conditional statements,

```python
if prompt_name == "research":
    ...
elif prompt_name == "summary":
    ...
```

the application delegates template selection to the Prompt Registry.

Example:

```python
PromptRegistry.get_prompt("summary")
```

Benefits:

- Centralized template management
- Reduced coupling
- Easy extensibility
- Cleaner business logic
- Open/Closed Principle compliance

---

# Alternatives Considered

## Option 1 — If/Else Prompt Selection

Example

```python
if prompt == "research":
    ...
elif prompt == "summary":
    ...
```

### Pros

- Simple implementation

### Cons

- Difficult to maintain
- Frequent modifications
- Violates Open/Closed Principle
- Large conditional blocks

---

## Option 2 — Dynamic Imports

Load prompt classes dynamically using module imports.

### Pros

- Highly flexible

### Cons

- Harder to debug
- Less IDE support
- More complex implementation

---

## Option 3 — Prompt Registry (Chosen)

Store prompt templates inside a centralized registry.

### Pros

- Simple
- Explicit
- Easy to test
- Easy to extend
- Clear architecture

### Cons

- Requires manual registration of new prompts

---

# Trade-offs

The Registry Pattern introduces an additional abstraction layer.

While this slightly increases the number of project components, it significantly improves scalability and keeps business logic independent of prompt implementations.

This trade-off favors long-term maintainability.

---

# Testing Performed

Comprehensive unit tests were added to validate prompt registration.

Verified components:

- FakeProvider
- ChatService
- PromptManager
- PromptRegistry

Prompt Registry tests verify:

- Research prompt registration
- Summary prompt registration
- QA prompt registration
- Code Review prompt registration

Test Result:

```
7 passed
```

All tests execute locally without internet connectivity or LLM API access.

---

# Challenges Encountered

## Duplicate Prompt Implementation

During development, an older implementation of `research_prompt.py` remained in the project.

This created confusion because two prompt implementations existed simultaneously.

The issue was resolved by:

- identifying duplicate files,
- removing obsolete implementations,
- maintaining a single source of truth inside the `templates` package.

---

## Unit Test Stability

Initial tests validated exact prompt wording.

This made tests fragile because even minor wording improvements caused failures.

Assertions were updated to validate important semantic content rather than exact formatting, resulting in more maintainable tests.

---

# Lessons Learned

This sprint reinforced several engineering principles:

- Centralize object discovery through registries.
- Avoid conditional logic for component selection.
- Design for extension rather than modification.
- Keep business logic independent of implementation details.
- Write automated tests for architectural components.

---

# Interview Takeaways

### Why use a Prompt Registry?

A Prompt Registry centralizes prompt discovery and removes conditional logic from business services.

It allows new prompt templates to be introduced without modifying existing application logic.

---

### Which design pattern is demonstrated?

Registry Pattern.

The registry maintains mappings between prompt identifiers and prompt implementations.

---

### Which SOLID principle is demonstrated?

Open/Closed Principle.

The application is open for extension by adding new prompt templates while remaining closed for modification.

---

### Why not use if/else?

Large conditional blocks become difficult to maintain as the number of prompt types increases.

The Registry Pattern provides a cleaner and more scalable solution.

---

# Deliverables

✅ SummaryPrompt

✅ QAPrompt

✅ CodeReviewPrompt

✅ Prompt Registry expansion

✅ Registry unit tests

✅ Seven passing unit tests

---

# Code Review Feedback

### What Went Well

- Clear separation of prompt responsibilities.
- Consistent prompt template structure.
- Registry implementation follows clean architecture.
- Automated tests validate registry behavior.
- No business logic changes were required.

### Improvements Identified

Future prompt templates should inherit from a common BasePrompt interface.

This will ensure all templates expose a consistent API and support metadata such as version, description, and supported use cases.

---

# Future Improvements

Planned enhancements include:

- BasePrompt abstract class
- Prompt metadata
- Prompt versioning
- Prompt listing API
- Prompt validation
- Dynamic prompt discovery

These improvements will prepare the framework for large-scale Agentic AI workflows.

---

# Sprint Deliverables Summary

- Multiple Prompt Templates
- Central Prompt Registry
- Registry-based Prompt Discovery
- Prompt Framework Expansion
- Automated Unit Tests
- Seven Passing Tests

---

# Sprint Status

**Completed ✅**

---

# Next Sprint

## Sprint 07 — Tool Framework

Upcoming work includes:

- Base Tool interface
- Tool Registry
- Calculator Tool
- DateTime Tool
- Weather Tool (Mock)
- Tool execution engine
- Tool unit testing

This sprint marks the transition from an AI assistant that only generates text to an Agentic AI capable of performing real-world actions.