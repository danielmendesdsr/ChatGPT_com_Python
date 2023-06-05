import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configurar o Selenium para utilizar o navegador Chrome
driver = webdriver.Chrome()

# URL da página
url = "https://produto.mercadolivre.com.br/MLB-2191179762-bicicleta-aro-29-krw-aluminio-24-vel-freio-a-disco-x42-_JM#is_advertising=true&position=2&search_layout=stack&type=pad&tracking_id=6c6fadb7-35cd-4b92-8d79-19e78ccabf31&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=2&ad_click_id=NDE5M2E2MzYtNDM5Zi00ZmZlLWJjOTItMjUxZDIxOTRjMTFh"

# Abrir a página
driver.get(url)

# Aguardar 5 segundos até que a página seja carregada
time.sleep(5)

# Localizar o elemento HTML que contém o preço do produto
elemento_preco = driver.find_element(By.XPATH, "//span[@class='andes-money-amount__fraction']")

# Obter o valor do preço
preco = float(elemento_preco.text)

# Verificar se o preço é menor que R$1000,00
if preco < 1000:
    print("Está disponível para compra.")
else:
    print("Aguarde, o preço está acima de R$1000,00.")

# Fechar o navegador
driver.quit()