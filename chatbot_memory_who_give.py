from langchain_ollama import OllamaLLM


model = OllamaLLM(
    base_url="http://localhost:11434",
    model="llama2"
)

chat_store= {}
chat_history = []
count=1
while True:
    user_input=input('You: ')
    chat_store[f"user{count}"]=user_input
    chat_history.append(user_input)
    if user_input=='exit':
        break

    result = model.invoke(chat_history)
    chat_store[f"AI{count}"]=result
    chat_history.append(result)
    count+=1

    print('AI: ',result)


print(chat_store)