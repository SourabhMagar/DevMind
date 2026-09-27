# DevMind

> A local-first, open-source AI developer assistant.

DevMind is an AI-powered developer assistant designed to help developers understand, explore, search, and work with software repositories using locally running AI models.

The project is designed with a **local-first architecture**, allowing developers to run the core AI experience on their own machines without requiring a cloud AI provider.

## Goals

DevMind aims to help developers:

- Understand unfamiliar codebases
- Search and explore repositories
- Explain code and architecture
- Investigate potential bugs
- Retrieve relevant code and documentation
- Generate development suggestions
- Analyze Git changes
- Work with AI-powered developer tools
- Run AI models locally

## Local-First Architecture

The default DevMind architecture is designed around local execution.

```text
Developer
    |
    v
DevMind
    |
    +-- FastAPI
    |
    +-- Repository Tools
    |
    +-- Retrieval
    |
    +-- Local Storage
    |
    v
Ollama
    |
    v
Local LLM