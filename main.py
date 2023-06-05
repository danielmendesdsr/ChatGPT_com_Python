import openai

# Defina a sua chave de API do OpenAI
openai.api_key = "<sua chave-key do ChatGPT>"

def conversar_com_gpt(texto):
    resposta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=texto,
        max_tokens=50,
        n=1
        
    )
    
    return resposta.choices[0].text.strip()

# Início da conversa com o ChatGPT
print("Olá! Sou o ChatGPT. Como posso ajudar?")

while True:
    entrada = input("> ")

    if entrada.lower() == 'sair':
        print("Até logo!")
        break

    resposta_gpt = conversar_com_gpt(entrada)
    print(resposta_gpt)