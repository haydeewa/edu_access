# pip3 install beautifulsoup4
# pip3 install requests

import requests
from requests import get
from bs4 import BeautifulSoup

import os
# import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
import time
os.chdir(r'/Users/haydeewa/')
os.getcwd()


browser = webdriver.Chrome()

url = 'https://www.avito.ru/'


browser.get(url)

search_input = browser.find_element(By.CSS_SELECTOR, '#app > div > div.styles-singlePageWrapper-eKDyt > div > div.index-header-kdkEW.index-stickyHeader-WbpLL > div > div.index-search-xHvcz > div.index-form-ENoC5 > div.index-suggest-zkzTd > div > div > div > label.input-layout-input-layout-_HVr_.input-layout-size-s-COZ10.input-layout-text-align-left-U2OZJ.width-width-12-_MkqF.suggest-input-X6pqt.js-react-suggest > input')
search_input.send_keys('круги для плавания')

search_button = browser.find_element(By.CSS_SELECTOR, '#app > div > div.styles-singlePageWrapper-eKDyt > div > div.index-header-kdkEW.index-stickyHeader-WbpLL > div > div.index-search-xHvcz > div.index-form-ENoC5 > div.index-button-rtdlZ > button')
search_button.click()

results = browser.find_elements(By.CLASS_NAME, "iva-item-content-rejJg")

for result in results:
    print(result.text)
    print()


browser.quit()






























