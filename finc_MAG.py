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
path = 'Univer_mag.xlsx'
table = pd.read_excel(path, sheet_name='work')
login = 'KazNU-D1'
password = '123456'

# Авторизация
driver.get('http://88.204.170.212:8080/fc-ui/jsp/login.jsp')
driver.find_element_by_name('user').send_keys(login)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('/html/body').click()
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
sleep(2)
# ------

input()

for st in range(6):
    try:
        iin = table.loc[st]['iin']
    except:
        print('Список закончился')
        break
    datasert = table.loc[st]['datasert']
    lang = table.loc[st]['lang']
    number = table.loc[st]['number']
    date = table.loc[st]['date']
    try:
        driver.find_element_by_xpath(f"//*[contains(text(), '{iin}')]").click()
    except:
        print(iin)
        continue
    sleep(4)
    # Язык обучения
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[3]/td[2]/span/input[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[3]/td[2]/span/input[1]').clear()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[3]/td[2]/span/input[1]').send_keys(lang)
    # Номер приказа
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[5]/td[2]/input').send_keys(number)
    # Дата приказа
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[5]/td[4]/span/input[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[5]/td[4]/span/input[1]').clear()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[5]/td[4]/span/input[1]').send_keys(date)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/fieldset/legend').click()
    # Дата договора
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[6]/td[2]/span/input[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[6]/td[2]/span/input[1]').send_keys('02.09.2019')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/fieldset/legend').click()
    # Ожидаемыйы год окончания
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[7]/td[2]/span/input[1]').send_keys('2021')
    # Дата сертефиката
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[8]/td/fieldset/div/div/table/tbody/tr/td[6]/span/input[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[8]/td/fieldset/div/div/table/tbody/tr/td[6]/span/input[1]').send_keys(datasert)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[3]/div/a[1]/span/span[1]').click()

