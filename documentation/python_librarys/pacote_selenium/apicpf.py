from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import os
import bs4
import requests
from time import sleep
currentdir = Path(__file__).parent
True_Data = []

with open((currentdir / 'cpf.txt').__str__(), 'r', encoding='utf-8') as textfile:
    dados = textfile.readlines()



chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.path.join('chrome_4test', 'chrome.exe')
chrome_service = Service(currentdir / 'drivers' / 'chromedriver.exe') #Arquivo webdriver a ser utilizado

chrome = webdriver.Chrome(chrome_options, chrome_service)

chrome.get('https://www.situacao-cadastral.com/')

sleep(10)

    

count = 0
while True:
    for cpf in dados:
        chrome.find_element(By.ID, 'doc').send_keys(cpf)
        chrome.find_element(By.ID, 'doc').send_keys(Keys.ENTER)
        htmlparsed = bs4.BeautifulSoup(chrome.page_source, 'html.parser')


        chrome.page_source
        if htmlparsed.select_one('#texto'):
            input('Não deu certo a pesquisa')
        if htmlparsed.select_one('#mensagem'):
            dados.remove(cpf)
            print('Sem Retorno')
            chrome.find_element(By.ID, 'doc').clear()
            continue
        if htmlparsed.select_one('#resultado'):
            if result:=htmlparsed.select_one('#resultado > span.dados.situacao > span'):
                print(result)
                True_Data.append(cpf + '\n')

        if len(True_Data) >= 10:
            break
    
    if len(True_Data) >= 10:
        break
    sleep(3)


with open('cpfvalidos.txt', 'w', encoding='utf-8') as textfile:
    textfile.writelines(True_Data)

