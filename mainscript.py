from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
EXE_PATH = '/home/.../chromedriver'
driver = webdriver.Chrome(executable_path=EXE_PATH)
driver.get('https://www.binance.com/ru/nft/mystery-box/market?page=1&size=16&nftType=2&orderBy=amount_sort&orderType=1&serialNo=161809875411286016&tradeType=0')
s=input()

def f1():
    time.sleep(4)
    driver.get('https://www.binance.com/ru/nft/mystery-box/market?page=1&size=16&nftType=2&orderBy=amount_sort&orderType=1&serialNo=161809875411286016&tradeType=0')
    time.sleep(3)
    kortinki=driver.find_elements(By.CLASS_NAME,'css-1r8sfl')
    kortinka=kortinki[0]
    kortinka.click()

def f4():
    time.sleep(100)
    driver.get('https://www.binance.com/ru/nft/balance?tab=boxes')
    time.sleep(3)
    print(driver.current_url)
    f4l = driver.find_elements(By.CLASS_NAME, 'css-9ttqf6')
    f4l[0].click()

def f5():
    time.sleep(3)
    links = driver.find_elements(By.TAG_NAME, 'input')
    print(len(links))
    textField = links[2]
    textField.send_keys(2)
    textField.send_keys(0)
    time.sleep(10)
    buts=driver.find_elements(By.TAG_NAME, 'button')
    but=buts[1]
    but.click()
    time.sleep(2)
    buts2=driver.find_elements(By.TAG_NAME, 'button')
    but2=buts2[3]
    but2.click()
    time.sleep(5)


def f6():
    while True:
        driver.get('https://www.binance.com/ru/nft/balance?tab=boxes')
        time.sleep(5)
        stran=driver.find_elements(By.CLASS_NAME,'css-spihoj')
        strana=stran[1]
        strana.click()
        time.sleep(10)
        divi = driver.find_elements(By.CLASS_NAME,'css-ai3vol')
        if len(divi)==0:
            break
        time.sleep(100)
    driver.get('https://www.binance.com/ru/nft/mystery-box/market?page=1&size=16&nftType=2&orderBy=amount_sort&orderType=1&serialNo=161809875411286016&tradeType=0')
    time.sleep(6)

while True:
    f1()
    f4()
    f5()
    f6()