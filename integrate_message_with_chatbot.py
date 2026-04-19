from langchain_ollama import OllamaLLM
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage


model = OllamaLLM(
    base_url="http://localhost:11434",
    model="llama2"
)

chat_history = [SystemMessage(content='you are a helpful assistant')]

while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result))

    print('AI: ',result)


print(chat_history)