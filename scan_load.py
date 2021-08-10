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
import os


driver = webdriver.Firefox()
path = 'Univer_bac_dvij.xlsx'
table = pd.read_excel(path, sheet_name='work')
login = 'KazNU-D4'
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

files = os.listdir(r'C:\Users\new2r\Desktop\FinCenter\prikazi2')

for st in range(241):
    iin = str(table.loc[st]['iin'])
    number = table.loc[st]['number']
    try:
        driver.find_element_by_xpath(f"//*[contains(text(), '{iin}')]").click()
        driver.find_element_by_xpath(f"//*[contains(text(), '{iin}')]").click()
    except:
        print(iin)
        print('eror')
        sleep(5)
        continue
    driver.find_element_by_xpath(f"//*[contains(text(), '{iin}')]").click()
    sleep(1)
    numb = str(number)
    numb = numb.split(' ')[0]
    file = ''
    print(numb)
    for i in files:
        if numb == i.split(' ')[1]:
            file = i
            print(st)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td/div/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[3]/td[1]/fieldset/div/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[7]/span/input').send_keys(f'C:\\Users\\new2r\\Desktop\\FinCenter\\prikazi2\\{file}')
    except:
        print(f'{numb}')
        print()
        print('end')
    sleep(2)