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
login = 'KazNU-D2'
password = '123456'

# Авторизация
driver.get('http://88.204.170.212:8080/fc-ui/jsp/login.jsp')
driver.find_element_by_name('user').send_keys(login)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('/html/body').click()
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
input()
# ------
driver.find_element_by_xpath('/html/body/div[1]/div[6]/table/tbody/tr[2]/td/div[2]/div/div/table/tbody/tr/td[3]/h3/a').click()
input()
# try:
#     driver.find_element(By.LINK_TEXT, "Пользователь уже подключен к системе! Продолжить вход в Систему?").click()
#     alert = wait.until(expected_conditions.alert_is_present())
#     alert.accept()
# except:
#     print('lis')
# Переход к специальности
#driver.find_element_by_xpath('/html/body/div[20]/div[2]/div/ul/li/div').click()
sleep(2)
for st in range(333):
        spec = table.loc[st]['spec']
        iin = table.loc[st]['iin']
        datasert = table.loc[st]['datasert']
        form = table.loc[st]['form']
        lang = table.loc[st]['lang']
        number = table.loc[st]['number']
        date = table.loc[st]['date']
        try:
                driver.find_element_by_xpath(f"//*[contains(text(), '{iin}')]").click()
        except:
                print(iin)
                continue
        # Дата договора об образовании
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td/fieldset/div/div/table/tbody/tr/td[2]/span/input[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td/fieldset/div/div/table/tbody/tr/td[2]/span/input[1]').send_keys('01.09.2017')
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td/fieldset/div/div/table/tbody/tr/td[2]/span/input[1]').clear()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td/fieldset/div/div/table/tbody/tr/td[2]/span/input[1]').send_keys('01.09.2017')
        sleep(0.5)