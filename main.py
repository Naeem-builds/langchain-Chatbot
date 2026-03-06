from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.7
    )

response = llm.invoke("What is the SAN?")
print(response.content)