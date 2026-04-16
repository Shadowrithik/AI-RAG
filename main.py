# Import LLM and prompt tools
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Import your custom retriever (vector DB or any search system)
from vector import retriever


# Initialize the local LLM model (change model if needed)
model = OllamaLLM(model="llama3.2")


#  Generic Prompt Template
# You can modify:
# - "domain" → what your system specializes in (e.g., finance, fitness, coding)
# - Instructions → tone, format, depth of answer
template = """
You are an expert assistant in {domain}.

Use the following context to answer the question accurately.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{question}

Answer:
"""

# Create prompt object
prompt = ChatPromptTemplate.from_template(template)

# Chain = Prompt → Model
chain = prompt | model


#  Main Loop (CLI Interaction)
while True:
    print("\n-------------------------------")
    
    # Take user input
    question = input("Ask your question (q to quit): ")
    
    if question.lower() == "q":
        print("Exiting...")
        break

    #  Retrieve relevant data from vector DB / retriever
    # You can modify retriever logic depending on your backend
    context = retriever.invoke(question)

    #  Run the chain with inputs
    result = chain.invoke({
        "domain": "your domain here (e.g., restaurant, AI, health)",
        "context": context,
        "question": question
    })

    #  Output result
    print("\nAnswer:\n", result)
