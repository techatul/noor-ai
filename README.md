# Noor-AI: Enterprise Agent for Luxury Brand Management

**Noor-AI** is a production-ready AI agent designed to manage customer engagement and business inquiries for a professional makeup artistry brand. This project demonstrates a sophisticated implementation of **Retrieval-Augmented Generation (RAG)** using a modular, agentic architecture.

---

## 🏗 System Architecture

The system is designed with a "Security-First" approach, separating the API gateway from the agentic reasoning engine.

### Data Flow
1.  **Frontend:** A WordPress-integrated interface sends async requests via JavaScript.
2.  **API Layer (FastAPI):** Handles CORS, enforces `X-API-Key` security, and manages Pydantic-based validation.
3.  **Orchestration (LangGraph):** Manages stateful conversation flows and conditional logic via a compiled state machine.
4.  **Vector Engine (ChromaDB):** Performs semantic search using `all-MiniLM-L6-v2` embeddings.
5.  **Inference (Groq):** Leverages Llama-3 for high-speed, structured output generation.

### Agent Workflow (LangGraph)
The internal logic of the agent follows a strictly defined state machine to ensure reliability and traceability:

```mermaid
graph TD
    %% Define Nodes
    START((● START))
    RETRIEVE[Node: retrieve]
    GENERATE[Node: generate]
    END((● END))

    %% Define flow based on StateGraph
    START --> RETRIEVE
    RETRIEVE --> GENERATE
    GENERATE --> END

    %% Styling for a professional look
    classDef start_node fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef end_node fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px;
    classDef process fill:#ffffff,stroke:#333333,stroke-width:1px;

    class START start_node;
    class END end_node;
    class RETRIEVE,GENERATE process;
