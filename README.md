# 🤖 AI Research Assistant

> A production-oriented Agentic AI backend built with FastAPI, Provider Pattern, Dependency Injection, and modern software engineering practices.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![Testing](https://img.shields.io/badge/pytest-Passing-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Overview

AI Research Assistant is a backend platform for building intelligent AI agents.

Unlike simple chatbot applications, this project focuses on **production-quality software architecture** and is designed to evolve into a complete Agentic AI system with:

- Multi-provider LLM support
- LangGraph workflows
- Tool calling
- Retrieval-Augmented Generation (RAG)
- Long-term memory
- Production deployment

---

## 🏗️ Current Architecture

```text
                FastAPI
                   │
             Dependency Injection
                   │
             ChatService
                   │
              LLMManager
                   │
          Provider Factory
                   │
            Gemini Provider
```

---

## ✨ Features

### ✅ Backend

- FastAPI REST API
- Swagger Documentation
- Configuration Management
- Structured Logging

### ✅ AI Layer

- Gemini Provider
- Provider Factory Pattern
- LLM Manager
- Prompt Manager

### ✅ Engineering

- Dependency Injection
- Clean Architecture
- Service Layer
- Unit Testing
- Fake Provider
- GitHub Documentation

---

## 📂 Project Structure

```text
AI-RESEARCH-ASSISTANT/

app/
│
├── api/
├── core/
├── dependencies/
├── llm/
├── prompts/
├── services/
├── tools/
├── memory/
├── graph/
└── utils/

tests/
│
├── fakes/
└── unit/

docs/
```

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.14 |
| Framework | FastAPI |
| LLM | Google Gemini |
| Validation | Pydantic |
| Testing | Pytest |
| Logging | Python Logging |
| API Docs | Swagger/OpenAPI |

---

## 🧪 Running the Project

### Clone

```bash
git clone https://github.com/<csevaibhav>/ai-research-assistant.git

cd ai-research-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Server

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Running Tests

Run all tests

```bash
python -m pytest -v
```

Run a specific test

```bash
python -m pytest tests/unit/test_chat_service.py -v
```

---

## 🏛️ Software Engineering Concepts Used

- Provider Pattern
- Factory Pattern
- Dependency Injection
- Service Layer
- SOLID Principles
- Separation of Concerns
- Unit Testing
- Mocking

---

## 📚 Documentation

The project includes engineering documentation for every sprint.

```
docs/

engineering-decisions.md

sprint-01.md

sprint-02.md

sprint-03.md

sprint-04.md

sprint-05.md
```

---

## 🚀 Upcoming Features

- Prompt Versioning
- Tool Calling
- LangGraph
- RAG
- ChromaDB
- Redis Memory
- Multi-Agent Workflow
- Docker
- CI/CD
- Kubernetes Deployment

---

## 👨‍💻 Author

**Vaibhav Yadav**

Backend Software Engineer transitioning into Agentic AI Engineering.

---

## ⭐ Project Status

Current Version:

```
v0.5.0
```

Current Milestone:

```
Engineering Foundation Complete ✅
```

Next Milestone:

```
Prompt Engineering Framework
```