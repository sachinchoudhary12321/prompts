from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_ollama import OllamaLLM

model =OllamaLLM(
    base_url="http://localhost:11434",
    model="llama2"
)

message = [
    SystemMessage(content='you are a helpful assistant'),
    HumanMessage(content='tell me about langchain ')
]
result = model.invoke(message)
message.append(AIMessage(content=result))
print(message)