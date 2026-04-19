from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_ollama import OllamaLLM
model = OllamaLLM(
    base_url="http://localhost:11434",
    model="llama2"
)

chatTemplate = ChatPromptTemplate([
    SystemMessage(content='you are a {domain} expert'),
    HumanMessage(content='explain in simple terms, what is {topic}')
])


prompt = chatTemplate.invoke({'domain':'cricket','topic':'cover drive'})

print(prompt)