import ollama

model = ollama.load("Llama 7B")


prompt = "Tell me a joke"
response = model.generate(prompt)
print(response)