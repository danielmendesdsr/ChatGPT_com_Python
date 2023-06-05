import openai

# Defina a sua chave de API da OpenAI
openai.api_key = "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"


def obter_resposta(texto):
    resultado = openai.Image.create(
        prompt = texto,
        n=1,
        size='1024x1024'
        
    )
    return resultado
    
# Loop para conversar com o modelo
print("Bem-vindo ao DA-LE 2! Digite 'sair' para encerrar a conversa.")
while True:
    pergunta = input("Descreva o texto para gerar a figura ")

    if pergunta.lower() == 'sair':
        break

    resultado = obter_resposta(pergunta)
    print(resultado)
    