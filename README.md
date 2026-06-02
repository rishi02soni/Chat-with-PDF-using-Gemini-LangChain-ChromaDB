#  GenAI RAG Assistant
 
A Retrieval-Augmented Generation (RAG) application powered by:
  
- Google Gemini
- LangChain
- ChromaDB
- Streamlit
  
---
 
## Features

- PDF Upload
- Semantic Search
- Vector Database
- Question Answering
- Multi-document Support
- Source Citation Support

---

## Prerequisites

- Python 3.10+
- Docker
- Git
- Gemini API Key

---

## Installation

Clone repository:

```bash
git clone https://github.com/yourusername/genai-rag-assistant.git

cd genai-rag-assistant
```

Run setup:

```bash
chmod +x scripts/*.sh

./scripts/setup.sh
```

---

## Environment Variables

Create `.env`

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Running Application

```bash
./scripts/run.sh
```

Application starts on:

```text
http://localhost:8501
```

---

## Testing

```bash
./scripts/test.sh
```

---

## Deployment

```bash
./scripts/deploy.sh
```

---

## Cleanup

```bash
./scripts/clean.sh
```

---

## Architecture

```text
User
 ↓
Streamlit UI
 ↓
PDF Loader
 ↓
Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Retriever
 ↓
Gemini LLM
 ↓
Response
```

---

## Tech Stack

| Layer | Technology |
|---------|-----------|
| UI | Streamlit |
| LLM | Gemini |
| Framework | LangChain |
| Vector DB | ChromaDB |
| Language | Python |

---

## Folder Structure

```
genai-rag-assistant/
├── app.py
├── requirements.txt
├── README.md
├── scripts/
│   ├── setup.sh
│   ├── run.sh
│   ├── test.sh
│   ├── deploy.sh
│   └── clean.sh
└── db/
```

---

## Future Enhancements

- Agentic RAG
- LangGraph
- PostgreSQL
- Authentication
- Kubernetes Deployment
- Multi-Agent Workflows

---

## License

MIT License

---

## Author

Rishi Soni

AI/ML Engineer | GenAI Developer
