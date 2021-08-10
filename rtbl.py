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
login = 'KazNU-D3'
password = '123456'

# Авторизация
driver.get('http://88.204.170.212:8080/fc-ui/jsp/login.jsp')
driver.find_element_by_name('user').send_keys(login)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('/html/body').click()
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
input()
# ------
# try:
#     driver.find_element(By.LINK_TEXT, "Пользователь уже подключен к системе! Продолжить вход в Систему?").click()
#     alert = wait.until(expected_conditions.alert_is_present())
#     alert.accept()
# except:
#     print('lis')
# Переход к специальности
#driver.find_element_by_xpath('/html/body/div[20]/div[2]/div/ul/li/div').click()
sleep(2)
bl = 0
for st in range(1, 1000):
        while True:
                try:
                        driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{st}]/td[1]/div').click()
                        break
                except:
                        print('end')
                        continue

        sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[5]/td/div/table/tbody/tr[1]/td[1]/div/div/div/div[2]/div[1]/div/div/fieldset/div/div/table/tbody/tr[1]/td[1]/fieldset/div/div/table/tbody/tr[2]/td[2]/button').click()
        sleep(1)
        while True:
                try:
                        driver.find_element_by_xpath('/html/body/div[18]/div[2]/a').click()
                        break
                except:
                        continue
        sleep(1)