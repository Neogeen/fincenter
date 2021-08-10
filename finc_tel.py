from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import timeit as t
import pandas as pd


driver = webdriver.Firefox()
path = 'Univer.xlsx'
table = pd.read_excel(path, sheet_name='work')
login = 'KazNU-D5'
password = '123456'

# Авторизация
driver.get('http://88.204.170.212:8080/fc-ui/jsp/login.jsp')
driver.find_element_by_name('user').send_keys(login)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('/html/body').click()
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
input()

for st in range(390):
    try:
        iin = str(table.loc[st]['iin'])
    except:
        print(1)
    number = table.loc[st]['number']
    try:
        driver.find_element_by_xpath(f"//*[contains(text(), '{iin}')]").click()
    except:
        continue
    sleep(4)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[5]/td/div/table/tbody/tr[1]/td[1]/div/div/div/div[2]/div[1]/div/div/fieldset/div/div/table/tbody/tr[1]/td[2]/fieldset/div/div/table/tbody/tr[5]/td/textarea').send_keys(number)