"""
Bot destinado a automação de testes.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path
from time import sleep


currentdir = Path(__file__).parent
waybrowser = currentdir / "chrome" / 'chrome.exe'
waydriver = currentdir / "web_driver" / "chromedriver.exe"

browserconfig = webdriver.ChromeOptions()
browserconfig.binary_location = waybrowser.__str__()

webservice = Service(executable_path=waydriver)

browser = webdriver.Chrome(browserconfig, webservice)

browser.get('localhost:3001')
sleep(30)
