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
path = 'Univer_bac_dvij.xlsx'
table = pd.read_excel(path, sheet_name='work')
login = 'KazNU-D5'
password = '123456'

# Авторизация
driver.get('http://88.204.170.212:8080/fc-ui/jsp/login.jsp')
driver.find_element_by_name('user').send_keys(login)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('/html/body').click()
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
sleep(2)
end = 0
input()

for st in range(241):
    iin = str(table.loc[st]['iin'])
    number = str(table.loc[st]['number'])
    date = str(table.loc[st]['date'])
    suma = int(table.loc[st]['suma'])
    if len(iin) == 9:
        iin = '000' + iin
    if len(iin) == 10:
        iin = '00' + iin
    if len(iin) == 11:
        iin = '0' + iin
    if len(date) == 7:
        date = '0' + date
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/fieldset/div/div/table/tbody/tr[1]/td/div/table/tbody/tr/td[2]/input').clear()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/fieldset/div/div/table/tbody/tr[1]/td/div/table/tbody/tr/td[2]/input').send_keys(iin)
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/fieldset/div/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[1]/button/span').click()
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/fieldset/div/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[1]/button/span').click()
    except:
        end = 1
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/fieldset/div/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[1]/button/span').click()
    except:
        end = 2
    sleep(0.8)
    try:
         driver.switch_to.active_element()
    except:
        end = 4
    sleep(2)
    try:
        driver.find_element_by_xpath('/html/body/div[21]/div[3]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[1]/div')
    except:
        driver.find_element_by_xpath('/html/body/div[21]/div[4]/a[1]/span/span').click()
        continue
    driver.find_element_by_xpath('/html/body/div[21]/div[4]/a[1]/span/span').click()
    sleep(1)
    try:
        driver.find_element_by_xpath(f"//*[contains(text(), '{iin}')]")
    except:
        print(iin)
        continue

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[1]/td/div/table/tbody/tr/td[2]/span/input[1]').send_keys('Отчислен')
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/fieldset/legend').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]/input').send_keys(number)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[4]/span/input[1]').send_keys(date)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/fieldset/legend').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[6]/span/input[1]').send_keys('2021')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[3]/td/fieldset/div/div/table/tbody/tr/td[2]/span/input[1]').send_keys('за нарушение учебной дисциплины, правил внутреннего распорядка и Устава учебного заведения')
    webElement = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[3]/td/fieldset/div/div/table/tbody/tr/td[4]/span/input[1]')
    webElement.send_keys(Keys.CONTROL + "a")
    webElement.send_keys(Keys.DELETE)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[3]/td/fieldset/div/div/table/tbody/tr/td[4]/span/input[1]').send_keys(suma)
    # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td[1]/fieldset/legend').click()
    # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[3]/td/fieldset/div/div/table/tbody/tr/td[4]/span/input[1]').click()
    # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[3]/td/fieldset/div/div/table/tbody/tr/td[4]/span/input[1]').clear()
    # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[3]/td/fieldset/div/div/table/tbody/tr/td[4]/span/input[1]').send_keys(suma)
    # /html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[3]/td/fieldset/div/div/table/tbody/tr/td[4]/span/input[1]

