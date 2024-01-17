import pathlib
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

current_folder = pathlib.Path(__file__).parent
user = "NET_4885C4"
password = "30938C4885C4"
browser_config = webdriver.ChromeOptions()
browser_config.binary_location = (current_folder / 'chrome' / 'chrome.exe').__str__()
# browser_config.add_argument('--headless')

browser_service = Service(executable_path=(current_folder / "chromedriver" / 'chromedriver.exe').__str__())

browser = webdriver.Chrome(browser_config, browser_service)


def sleep_wireless(status: bool) -> None:
    browser.get('http://192.168.0.1/logout.html')
    sleep(5)
    box_user = browser.find_element(By.XPATH, '/html/body/div[2]/div/form/div[1]/div/input')
    box_user.send_keys(user)
    box_passwd = browser.find_element(By.XPATH, '/html/body/div[2]/div/form/div[2]/div/input')
    box_passwd.send_keys(password)

    box_submit = browser.find_element(By.XPATH, '/html/body/div[2]/div/form/div[3]/button/div')
    box_submit.click()
    sleep(5)

    browser.get('http://192.168.0.1/seguranca-controle-dos-pais-filtro-tod.html')
    sleep(5)

    """
    ip_status = htmlparsed.select_one("tod-table > tbody:nth-child(2) > tr > td:nth-child(7)")
    ip_status2 = htmlparsed.select_one("tod-table > tbody:nth-child(3) > tr > td:nth-child(7)")
    ip_status3 = htmlparsed.select_one("tod-table > tbody:nth-child(4) > tr > td:nth-child(7)")
    ip_status4 = htmlparsed.select_one("tod-table > tbody:nth-child(5) > tr > td:nth-child(7)")
    ip_status5 = htmlparsed.select_one("tod-table > tbody:nth-child(6) > tr > td:nth-child(7)")
    ip_status6 = htmlparsed.select_one("tod-table > tbody:nth-child(7) > tr > td:nth-child(7)")
    ip_status7 = htmlparsed.select_one("tod-table > tbody:nth-child(8) > tr > td:nth-child(7)")
    ip_status8 = htmlparsed.select_one("tod-table > tbody:nth-child(9) > tr > td:nth-child(7)")
    ip_status9 = htmlparsed.select_one("tod-table > tbody:nth-child(10) > tr > td:nth-child(7)")
    """
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
