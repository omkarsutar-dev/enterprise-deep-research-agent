# Enterprise Deep Research Agent

A production-oriented **multi-agent AI system** built using **LangGraph, OpenAI, RAG, ChromaDB, and Tavily Search**. The project combines planning, retrieval, critique, reflection, and memory to generate grounded and high-quality responses.

Inspired by modern agentic architectures such as OpenAI Deep Research.

---

## 🚀 Features

### Multi-Agent Architecture

* Planner Agent
* Research Agent
* Critic Agent
* Reflection Agent
* Memory Agent

### Retrieval-Augmented Generation (RAG)

* PDF document ingestion
* Semantic chunking
* OpenAI embeddings
* ChromaDB vector database
* Similarity search

### Web Search

* Tavily Search integration
* Latest information retrieval

### Memory

* Session memory
* Long-term memory
* Context-aware conversations

### Agentic Patterns

* Conditional routing
* Reflection loops
* Retry limits
* Structured outputs
* Self-correcting workflow

### Production Features

* FastAPI backend
* Typed state management
* Modular architecture
* Pydantic validation

---

# 🏗 Architecture

```text
                         User
                           │
                           ▼
                   Memory Agent
                           │
                           ▼
                   Planner Agent
                           │
                           ▼
                  Research Agent
                  /             \
                 /               \
        Tavily Search         Internal RAG
                                     │
                                 ChromaDB
                                     │
                                     ▼
                                  Answer
                                     │
                                     ▼
                               Critic Agent
                                     │
                          Score >= Threshold ?
                            /               \
                          Yes                No
                           │                  │
                           ▼                  ▼
                         END          Reflection Agent
                                              │
                                              ▼
                                       Research Agent
```

---

# 🤖 Agents

## Planner Agent

Breaks user queries into structured tasks.

## Research Agent

Combines web search and internal knowledge retrieval to generate grounded answers.

## Critic Agent

Evaluates responses for:

* Accuracy
* Completeness
* Hallucinations
* Missing information

## Reflection Agent

Improves responses using feedback from the Critic Agent.

## Memory Agent

Maintains session history and long-term memory.

---

# 🛠 Tech Stack

| Category        | Technology        |
| --------------- | ----------------- |
| Framework       | LangGraph         |
| LLM Framework   | LangChain         |
| Model           | GPT-4o-mini       |
| Embeddings      | OpenAI Embeddings |
| Vector Database | ChromaDB          |
| Web Search      | Tavily Search     |
| Backend         | FastAPI           |
| Validation      | Pydantic          |
| Language        | Python            |

---

# 📂 Project Structure

```text
backend/
│
├── agents/
│     ├── planner_agent.py
│     ├── research_agent.py
│     ├── critic_agent.py
│     ├── reflection_agent.py
│     ├── memory_agent.py
│
├── prompts/
│
├── tools/
│     ├── tavily_tool.py
│     ├── rag_tool.py
│
├── rag/
│     ├── ingest.py
│     ├── vector_store.py
│     ├── retriever.py
│
├── memory/
│     ├── session_memory.py
│     ├── long_term_memory.py
│
├── graphs/
│     ├── graph_builder.py
│     ├── router.py
│     ├── state.py
│
├── models/
│
├── llms/
│
├── documents/
│
├── vector_store/
│
├── api/
│
└── main.py
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/enterprise-deep-research-agent.git

cd enterprise-deep-research-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

# 🚀 Run the Application

Start FastAPI:

```bash
uvicorn backend.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Example Request

```json
{
    "query": "Explain Retrieval-Augmented Generation"
}
```

---

# Example Workflow

```text
User Query
      ↓
Planner Agent
      ↓
Research Agent
      ↓
Web Search + RAG
      ↓
Answer Generation
      ↓
Critic Agent
      ↓
Reflection Loop
      ↓
Final Response
```

---

# Key Concepts Demonstrated

* Agentic AI
* Multi-Agent Systems
* Retrieval-Augmented Generation
* Reflection and Self-Correction
* Long-Term Memory
* Tool Calling
* Conditional Graphs
* Structured Outputs
* Vector Databases
* Semantic Search

---

# Future Enhancements

* Hybrid Search
* Source Attribution
* Human-in-the-Loop (HITL)
* LangSmith Observability
* MCP Integration
* Parallel Research Agents
* Streamlit UI
* Docker Deployment
* Multi-modal Support
* Report Generation

---

# Built With 

* Python
* LangGraph
* LangChain
* OpenAI
* ChromaDB
* Tavily Search
* FastAPI
* Pydantic
