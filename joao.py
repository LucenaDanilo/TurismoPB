# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep

# options = Options()
# options.add_argument('--headless')
# navegador = webdriver.Chrome(options=options)
# navegador.maximize_window()

# link = navegador.get('https://web.whatsapp.com')
# sleep(30)
# link_qr = navegador.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div')


# print(link_qr.get_attribute('data-ref'))
import requests
from bs4 import BeautifulSoup
from time import sleep
# URL do site do WhatsApp Web (ou o site desejado)
# url = 'https://web.whatsapp.com/'

# # Realiza a requisição HTTP
# response = requests.get(url)

# # Verifica se a requisição foi bem-sucedida (código 200)
# if response.status_code == 200:
#     # Cria um objeto BeautifulSoup para analisar o HTML
#     soup = BeautifulSoup(response.text, 'html.parser')
#     sleep(30)
#     # Encontra o elemento desejado (substitua pelo seletor específico)
#     elemento_desejado = soup.find('id', '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div')

#     # Extrai o ID do elemento
#     if elemento_desejado:
#         id_do_elemento = elemento_desejado.get('data-ref')
#         print(f'O ID do elemento é: {id_do_elemento}')
#     else:
#         print('Elemento não encontrado')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Configuração para modo headless
chrome_options = Options()
chrome_options.add_argument('--headless')

# Inicializa o WebDriver com as opções headless
driver = webdriver.Chrome(options=chrome_options)

# Abre a página
driver.get('https://web.whatsapp.com/')

# Define um tempo de espera (aumente se necessário)
tempo_de_espera = 20

try:
    # Espera até que o elemento desejado seja visível na página
    elemento_desejado = WebDriverWait(driver, tempo_de_espera).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div'))
    )

    # Extrai o conteúdo do elemento
    conteudo_do_elemento = elemento_desejado.text
    print(f'O conteúdo do elemento é: {conteudo_do_elemento}')

except Exception as e:
    print(f'Erro ao esperar pelo elemento: {str(e)}')

finally:
    # Fecha o navegador
    driver.quit()