import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import os
from urllib.parse import urlparse
import re

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

#--------------------------------------------------- task 3 -------------------------------------------------------------------

def total_price():
    browser.get('https://www.nemlig.com')
    browser.implicitly_wait(2)
    browser.maximize_window()

    items = ['gær', 'minimælk', 'banan', 'tomatpasta']
    integer_prices = []
    decimal_prices = []

    searchField = browser.find_element_by_xpath('//*[@id="site-header-search-field-main"]')
    searchField.click()
    for item in items:
        searchField.send_keys(item)
        searchField.submit()
        browser.implicitly_wait(2)
        
        integer_price = float(browser.find_element_by_xpath('//*[@id="searchscrollable"]/div/searchresult/div[1]/div[3]/div[1]/div[1]/div[1]/productlist-item[1]/a/div/div[3]/pricecontainer/div/div[2]/span').text)
        integer_prices.append(integer_price)
    
        decimal_price = float(browser.find_element_by_xpath('//*[@id="searchscrollable"]/div/searchresult/div[1]/div[3]/div[1]/div[1]/div[1]/productlist-item[1]/a/div/div[3]/pricecontainer/div/div[2]/sup').text)/100
        decimal_prices.append(decimal_price)

        searchField.clear()
    
    item_prices = np.add(integer_prices, decimal_prices)
    total = 0
    for i in range(0, len(item_prices)):    
       total = total + item_prices[i];    
    print(str(total) + ' kr.')
    return total 

#total_price()