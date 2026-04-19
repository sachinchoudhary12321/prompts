from langchain_ollama import OllamaLLM


model = OllamaLLM(
    base_url="http://localhost:11434",
    model="llama2"
)

while True:
    user_input=input('You: ')
    if user_input=='exit':
        break

    result = model.invoke(user_input)
    print('AI: ',result)