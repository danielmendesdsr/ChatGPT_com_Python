import os
from PyPDF2 import PdfMerger

# Caminho dos arquivos PDF
pasta_pdf = r"D:\Python\ChatGPT4\Aula5\pdf"
caminho_arquivo_saida = r"D:\Python\ChatGPT4\Aula5\pdf\pdf_final.pdf"

# Inicializar o objeto do PdfMerger
merger = PdfMerger()

# Percorrer os arquivos PDF na pasta
for nome_arquivo in os.listdir(pasta_pdf):
    if nome_arquivo.endswith(".pdf"):
        caminho_arquivo = os.path.join(pasta_pdf, nome_arquivo)
        merger.append(caminho_arquivo)

# Salvar o arquivo PDF final
merger.write(caminho_arquivo_saida)
merger.close()

print("Os arquivos PDF foram juntados com sucesso!")

