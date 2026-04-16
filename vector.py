#  Import embeddings + vector store
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

#  Utilities
import os
import pandas as pd


#  Load your dataset
# Replace with your own file (CSV, JSON, etc.)
DATA_PATH = "your_data.csv"
df = pd.read_csv(DATA_PATH)


#  Initialize embedding model
# Change model if needed (e.g., OpenAI, HuggingFace)
embeddings = OllamaEmbeddings(model="mxbai-embed-large")


#  Define where vector DB will be stored
DB_LOCATION = "./chroma_langchain_db"

# If DB doesn't exist → create + add documents
add_documents = not os.path.exists(DB_LOCATION)


#  Convert data into LangChain Documents
# Modify this section depending on your dataset structure
documents = []
ids = []

if add_documents:
    for i, row in df.iterrows():
        
        #  Combine relevant fields into one text
        content = f"{row['Title']} {row['Review']}"  # Modify fields here
        
        #  Add metadata (optional but powerful for filtering/search)
        metadata = {
            "rating": row.get("Rating"),
            "date": row.get("Date")
        }

        document = Document(
            page_content=content,
            metadata=metadata,
            id=str(i)
        )

        documents.append(document)
        ids.append(str(i))


#  Create / Load vector store
vector_store = Chroma(
    collection_name="your_collection_name",  # Change based on project
    persist_directory=DB_LOCATION,
    embedding_function=embeddings
)


#  Add documents only if DB is new
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)


#  Create retriever
# k = number of relevant chunks to fetch
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)
