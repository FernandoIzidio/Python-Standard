"""
Selenium é um pacote muito util para automação web, e testes automaticos de sites
Webdriver-manager - Facilita na instalação de um webdriver, ele permite que não seja necessário baixar um webdriver como serviço

chromedrivermanager().install() - Sobe um servidor webdriver para ser usado pelo service

webdriver.browser - Define qual navageador será usado



options - Define as configurações dos testes
webdriver.webdriver.chrome.service.Service - Define o webdriver a ser utilizado, 



metódos e atributos de chromeopt:
    addargument("") - Adicoina uma configuração no chrome durante o processo de exucução.
        configs:
            --headless - Não abre a interface do navegador durante a execução

    binary_location - Define o caminho de qual chrome vai ser executado


Metódos e atributos de webdriver.browsername(service=chrome_service(exec), options=(chrome_options)):
    get(url) - Abre um site

"""

from pathlib import Path
from time import sleep
import os.path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
currentdir = Path(__file__).parent
chrome_binary = Path(os.path.join("C:\\Users", 'Ferna', 'OneDrive', 'Área de Trabalho', 'chrome_4test'), 'chrome.exe')
chromedriver = currentdir / "drivers" / "chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_binary.__str__()

chrome_service = Service(executable_path=chromedriver.__str__())

chrome_browser = webdriver.Chrome(
    service=chrome_service, options=chrome_options
)

chrome = chrome_browser

chrome.get('https://www.google.com.br')
#search_input = WebDriverWait(chrome, TIME_TO_WAIT).until(expected_conditions.presence_of_element_located((By.ID, 'APjFqb')))
sleep(10)

chrome.find_element(By.ID, 'APjFqb').send_keys('Situação Cadastral')
chrome.find_element(By.ID, 'APjFqb').send_keys(Keys.ENTER)
result = chrome.find_element(By.ID, 'rcnt')
links = result.find_elements(By.TAG_NAME, 'a')
links[1].click()
#chrome.find_element(By.NAME, 'btnK').submit()


input()