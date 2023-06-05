import openai
from googletrans import Translator
from fpdf import FPDF
import os
import unicodedata


openai.api_key ="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"


diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual, "audio/voz.mp3")

audio_file = open(caminho_arquivo, "rb")

resultado = openai.Audio.transcribe("whisper-1", audio_file)
texto_originado = resultado['text']
print (texto_originado)

# Crie uma classe personalizada para o PDF
class PDF(FPDF):
    def header(self):
        # Cabeçalho do PDF
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Título do Documento', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        # Rodapé do PDF
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')



# Adicionar o texto ao PDF
texto_formatado = ''.join(c for c in unicodedata.normalize('NFKD', texto_originado) if not unicodedata.combining(c))

# Opções de idioma para tradução
opcoes_idioma = ['Inglês', 'Português (Brasil)', 'Espanhol']

# Exibir as opções para o usuário
print("Por favor, escolha um idioma para traduzir o texto:")
for i, idioma in enumerate(opcoes_idioma):
    print(f"{i+1}. {idioma}")

# Solicitar a escolha do usuário
escolha = int(input("Opção: ")) - 1

# Verificar a escolha do usuário e realizar a tradução
if escolha == 0:
    idioma_destino = 'en'
elif escolha == 1:
    idioma_destino = 'pt'
elif escolha == 2:
    idioma_destino = 'es'
else:
    print("Opção inválida. Nenhuma tradução será realizada.")
    idioma_destino = None

# Realizar a tradução, se necessário
if idioma_destino:
    tradutor = Translator()
    texto_traduzido = tradutor.translate(texto_formatado, dest=idioma_destino).text

    # Exibir o texto traduzido
    print("\nTexto traduzido:")
    print(texto_traduzido)

# Crie uma classe personalizada para o PDF
class PDF(FPDF):
    def header(self):
        # Cabeçalho do PDF
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Título do Documento', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        # Rodapé do PDF
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')

# Criar uma instância do PDF
pdf = PDF()

# Adicionar uma página
pdf.add_page()

# Definir a fonte e o tamanho do texto
pdf.set_font('Arial', '', 12)

# Adicionar o texto ao PDF
texto_formatado = ''.join(c for c in unicodedata.normalize('NFKD', texto_traduzido) if not unicodedata.combining(c))
pdf.multi_cell(0, 10, texto_formatado)

# Salvar o PDF
caminho_pasta_docs = os.path.join(diretorio_atual, 'docs')
nome_arquivo_pdf = 'arquivotraduzido.pdf'
caminho_arquivo_pdf = os.path.join(caminho_pasta_docs, nome_arquivo_pdf)
pdf.output(caminho_arquivo_pdf)
