import pathlib
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

CURRENT_FOLDER = pathlib.Path(__file__).parent
USER = "NET_4B85C4"
PASSWORD = "3093BC4B85C4"
browser_config = webdriver.ChromeOptions()
browser_config.binary_location = (current_folder / 'chrome' / 'chrome.exe').__str__()
# browser_config.add_argument('--headless')

browser_service = Service(executable_path=(current_folder / "chromedriver" / 'chromedriver.exe').__str__())

browser = webdriver.Chrome(browser_config, browser_service)
def sleep_wireless(status:bool) -> None:
    browser.get('http://192.168.0.1/')
    browser.implicitly_wait(5)
    
    box_user = browser.find_element(By.XPATH, '/html/body/div[2]/div/form/div[1]/div/input')
    box_user.send_keys(user)
    box_passwd = browser.find_element(By.XPATH, '/html/body/div[2]/div/form/div[2]/div/input')
    box_passwd.send_keys(password)

    box_submit = browser.find_element(By.XPATH, '/html/body/div[2]/div/form/div[3]/button/div')
    box_submit.click()
    sleep(5)

    browser.get('http://192.168.0.1/seguranca-controle-dos-pais-filtro-tod.html')
    sleep(5)
    

    if status:
        for ip_index in range(1, 10):
            ip_config = browser.find_element(By.XPATH,
                                             f'/html/body/div[2]/div/div[2]/div/div/form/ul/table/tbody[{ip_index}]/tr/td[17]/input')
            ip_config.click()
            sleep(5)

            sleep_time = browser.find_element(By.XPATH,
                                              '/html/body/div[2]/div/div[2]/div/div/form/div[10]/div/div/select')
            sleep_time.click()

            activeopt = browser.find_element(By.XPATH,
                                             '/html/body/div[2]/div/div[2]/div/div/form/div[10]/div/div/select/option[2]')
            activeopt.click()
            submit_config = browser.find_element(By.XPATH,
                                                 '/html/body/div[2]/div/div[2]/div/div/form/div[11]/button/div')
            submit_config.click()
            print(f'Ativando o ip_{ip_index}')
            sleep(5)

    else:
        for ip_index in range(1, 10):
            ip_config = browser.find_element(By.XPATH,
                                             f'/html/body/div[2]/div/div[2]/div/div/form/ul/table/tbody[{ip_index}]/tr/td[17]/input')
            ip_config.click()
            sleep(5)

            sleep_time = browser.find_element(By.XPATH,
                                              '/html/body/div[2]/div/div[2]/div/div/form/div[10]/div/div/select')
            sleep_time.click()

            activeopt = browser.find_element(By.XPATH,
                                             '/html/body/div[2]/div/div[2]/div/div/form/div[10]/div/div/select/option[3]')
            activeopt.click()
            submit_config = browser.find_element(By.XPATH,
                                                 '/html/body/div[2]/div/div[2]/div/div/form/div[11]/button/div')
            submit_config.click()
            print(f'Desativando o ip_{ip_index}')
            sleep(5)

    browser.get('http://192.168.0.1/configuracao-rapida.html')
    sleep(5)
    exit_box = browser.find_element(By.XPATH, '/html/body/div[2]/div/a[2]')
    exit_box.click()


while True:
    opt = int(input('Digite 0 para desativar.\nDigite 1 para ativar\n:'))
    if opt in range(0, 2):
        break

sleep_wireless(opt)
