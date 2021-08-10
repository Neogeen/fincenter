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
path = 'Univer_doc.xlsx'
table = pd.read_excel(path, sheet_name='work')
login = 'KazNU-D2'
password = '123456'

# Авторизация
driver.get('http://88.204.170.212:8080/fc-ui/jsp/login.jsp')
driver.find_element_by_name('user').send_keys(login)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('/html/body').click()
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
sleep(2)
block_init = 23
input()
# /html/body/div[23]/div[2]/a
# ------
for st in range(408):
    spec = table.loc[st]['spec']
    iin = str(table.loc[st]['iin'])
    obl = table.loc[st]['obl']
    lang = table.loc[st]['lang']
    number = table.loc[st]['number']
    date = table.loc[st]['date']
    # Ввод иина
    sleep(3)
    driver.find_element_by_xpath('//*[@id="a42e4cf7-0fb7-4156-82eb-0d2b1eba6836"]').send_keys(iin)
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/fieldset/div/div/div/table/tbody/tr/td[3]/button').click()
    sleep(1)
    while True:
        try:
            driver.find_element_by_xpath(f'/html/body/div[{block_init}]/div[2]/a').click()
            # /html/body/div[22]/div[2]/a
            break
        except:
            a = input()
            block_init = a
            break
    # Форма обучения
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[2]/td[2]/span/input[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[2]/td[2]/span/input[1]').send_keys('очная')
    # Язык обучения
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[3]/td[2]/span/input[1]').send_keys(lang)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/fieldset/legend').click()
    # Номер приказа
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[5]/td[2]/input').send_keys(number)
    # Дата приказа
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[5]/td[4]/span/input[1]').send_keys(date)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/fieldset/legend').click()
    # Дата договора
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[6]/td[2]/span/input[1]').send_keys('01.09.2018')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/fieldset/legend').click()
    # Год окончания
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td[1]/fieldset/div/div/div/table/tbody/tr[7]/td[2]/span/input[1]').send_keys('2021')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[4]/td/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/fieldset/legend').click()
    # Специальность
    driver.find_element_by_xpath('//*[@id="663719a1-6c4b-4ba7-b5a0-3893e6145562"]').click()
    sleep(1)
    try:
        driver.switch_to.active_element()
    except:
        print('NOPE')
    block_number = 0
    # /html/body/div[23]/div[2]/div/ul/li/ul/li[3]/ul/li[1]/div/span[5]
    # /html/body/div[22]/div[2]/div/ul/li/ul/li[3]/ul/li[1]/div/span[5]
    # /html/body/div[23]/div[2]/a
    for i in range(1, 12):
        text = driver.find_element_by_xpath(f'/html/body/div[{block_init}]/div[2]/div/ul/li/ul/li[3]/ul/li[{i}]/div/span[5]').text
        if text == obl:
            block_number = i
            break
    j = 1
    while True:
        text1 = driver.find_element_by_xpath(f'/html/body/div[{block_init}]/div[2]/div/ul/li/ul/li[3]/ul/li[{block_number}]/ul/li[{j}]/div/span[6]').text
        if spec == text1:
            driver.find_element_by_xpath(f'/html/body/div[{block_init}]/div[2]/div/ul/li/ul/li[3]/ul/li[{block_number}]/ul/li[{j}]/div/span[6]').click()
            break
        j += 1
    driver.find_element_by_xpath(f'/html/body/div[{block_init}]/div[3]/a[1]/span/span').click()
    driver.switch_to.window(driver.current_window_handle)


