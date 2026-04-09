# AI-RAG

## What this project does
AI-RAG is a **Retrieval-Augmented Generation (RAG)** project that lets you chat with your own data. Instead of relying only on the LLM’s built-in knowledge, it:

1. **Ingests your documents** (text/markdown/pdf/etc. depending on your pipeline)
2. **Splits** them into smaller chunks
3. **Embeds** those chunks into vectors
4. **Stores** vectors in a vector database / index
5. On a question, **retrieves** the most relevant chunks
6. Sends the retrieved context to a **local Ollama model** to generate a grounded answer

This improves accuracy and reduces hallucinations because the model answers using the retrieved context.

## Tech stack
- **Language:** Python
- **LLM runtime:** **Ollama** (local LLM serving)
- **RAG components (typical):**
  - Document loading / parsing
  - Text chunking
  - Embeddings model
  - Vector store (FAISS/Chroma/etc.)
  - Retriever + prompt template
  - LLM response generation

> If your repo uses a specific framework (LangChain / LlamaIndex / Haystack), you can add it here.

## Model (Ollama)
This project is designed to work with models served by Ollama, for example:
- `llama3`
- `mistral`
- `phi3`

**Configure the model name** in your config or environment variables (see below).

## Python version
Recommended: **Python 3.10+** (3.10 or 3.11 is ideal for most RAG stacks).

If your project is pinned to a specific version, update this section accordingly.

## Efficiency notes
RAG efficiency depends on:
- **Chunk size & overlap** (tradeoff between context quality and index size)
- **Embedding model speed** (CPU vs GPU)
- **Vector store choice** (FAISS is fast locally; others may offer persistence)
- **Top-k retrieval** (smaller k is faster; larger k may improve answers)

Common optimizations:
- Cache embeddings so you don’t re-embed unchanged docs
- Use a persistent vector store
- Use streaming responses from the LLM

## Setup

### 1) Clone the repository
```bash
git clone https://github.com/Shadowrithik/AI-RAG.git
cd AI-RAG
```

### 2) Create & activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3) Install dependencies
If you have `requirements.txt`:
```bash
pip install -r requirements.txt
```

If you use Poetry:
```bash
poetry install
```

### 4) Install and run Ollama
Install Ollama from its official site and pull a model:
```bash
ollama pull llama3
```

Start Ollama (usually it runs as a background service). Test it:
```bash
ollama list
```

### 5) Configure environment variables
Create a `.env` file (or export env vars) with values your app expects. Example:
```env
OLLAMA_MODEL=llama3
# Optional examples (rename to match your code)
CHUNK_SIZE=800
CHUNK_OVERLAP=100
TOP_K=4
```

## How to use

### Ingest / index your documents
Run your ingestion script/command (replace with your actual command):
```bash
python ingest.py --source ./data
```

### Ask questions
Run the app (replace with your entrypoint):
```bash
python app.py
```

Example prompt:
- “Summarize the documents in my dataset.”
- “What does this project do?”

## Customize
You can customize AI-RAG by changing:

- **Data sources**: add new loaders/parsers (PDF, webpages, etc.)
- **Chunking**: tune chunk size & overlap
- **Embeddings**: swap embedding model for better quality/speed
- **Vector store**: FAISS/Chroma/etc.
- **Prompt**: change the system prompt and how retrieved context is inserted
- **Retriever**: similarity search vs MMR, filters, metadata, top-k
- **Ollama model**: choose a faster or smarter local model

## Project structure (optional)
Add your actual folder layout here once finalized, for example:
```
AI-RAG/
  data/
  ingest.py
  app.py
  requirements.txt
  README.md
```

## Contributing
PRs are welcome. Open an issue for major changes.

## License
Add a license file (MIT/Apache-2.0/etc.) and reference it here.