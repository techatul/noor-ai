# Noor-AI: Enterprise Agent for Luxury Brand Management

**Noor-AI** is a production-ready AI agent designed to manage customer engagement and business inquiries for a professional makeup artistry brand. This project demonstrates a sophisticated implementation of **Retrieval-Augmented Generation (RAG)** using a modular, agentic architecture.

---

## System Architecture

The system is designed with a "Security-First" approach, separating the API gateway from the agentic reasoning engine.

### Data Flow
1. **Frontend:** A WordPress-integrated interface sends async requests via JavaScript.
2. **API Layer (FastAPI):** Handles CORS, enforces `X-API-Key` security, and manages Pydantic-based validation.
3. **Orchestration (LangGraph):** Manages stateful conversation flows and conditional logic.
4. **Vector Engine (ChromaDB):** Performs semantic search using `all-MiniLM-L6-v2` embeddings.
5. **Inference (Groq):** Leverages Llama-3 for high-speed, structured output generation.

```mermaid
graph TD
    A[WordPress Client] -->|POST /api/v1/message| B(FastAPI Gateway)
    B -->|API Key Validation| C{LangGraph Orchestrator}
    C -->|Semantic Search| D[(ChromaDB Vector Store)]
    D -->|Contextual Docs| C
    C -->|Prompt + Context| E[Groq LLM]
    E -->|Structured JSON| C
    C -->|AssistantResponse| B
    B -->|Final JSON| A
