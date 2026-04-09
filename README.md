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
This project is designed to work with **any model served by Ollama**.

If your laptop/PC is low-spec, prefer smaller/faster models such as:
- `mistral`
- `gemma`

You can also use other models like `llama3` depending on your hardware.

**Configure the model name** in your config or environment variables (see below).

## Python version (required)
**Python 3.11.x is required.**

> If you use any other Python version, the project may not run correctly.

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

### 2) Create a Python 3.11 virtual environment (required)
Make sure `python` points to Python **3.11.x**:
```bash
python --version
```

Create a virtual environment:
```bash
python -m venv .venv
```

Activate it:

**Windows (PowerShell):**
```bash
.\.venv\Scripts\Activate.ps1
```

**Windows (cmd):**
```bash
.\.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

Upgrade pip:
```bash
python -m pip install --upgrade pip
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
Install Ollama from its official site and pull a model.

Low-spec recommendation:
```bash
ollama pull mistral
# or
ollama pull gemma
```

Start Ollama (usually it runs as a background service). Test it:
```bash
ollama list
```

### 5) Configure environment variables
Create a `.env` file (or export env vars) with values your app expects. Example:
```env
OLLAMA_MODEL=mistral
# Optional examples (rename to match your code)
CHUNK_SIZE=800
CHUNK_OVERLAP=100
TOP_K=4
```

## How to run

> The exact entrypoint can differ by repo structure. If you have different file names, update the commands below.

### Ingest / index your documents
Run your ingestion script/command (replace with your actual command):
```bash
python ingest.py --source ./data
```

### Start the app
Run the app (replace with your entrypoint):
```bash
python app.py
```

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
