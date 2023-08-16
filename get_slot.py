import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time

browser = webdriver.Chrome()
url = 'https://edu.21-school.ru'
browser.get(url)

login = browser.find_element(By.CSS_SELECTOR, '#mui-1')
login.send_keys('haydeewa@student.21-school.ru')

password = browser.find_element(By.CSS_SELECTOR, '#mui-2')
password.send_keys('ReforM2021!')

enter = browser.find_element(By.CSS_SELECTOR, '#login > div.jss1 > div > div.jss4 > div > div > form > div.jss22 > button')
enter.click()

time.sleep(2)

calendar = browser.find_element(By.LINK_TEXT, "Calendar")
calendar.click()

time.sleep(5)

slots = browser.find_elements(By.CSS_SELECTOR, "[data-testid='ProjectTimeSlot.IndividualProject green']")
for slot in slots:
    slot.click()
    time.sleep(2)

time.sleep(5)

# xpath = []


# for i in range(1, 8):
#     xpath.append('//*[@id="root"]/div[4]/div/div[2]/div[' + str(i) + ']')
#
# slot_containers = []
#
# for path in xpath:
#     print(path)
#     slot = browser.find_element(By.XPATH, path)
#     slot_containers.append(slot)
#
#
# for container in slot_containers:
#     print("tut")
#
#     # slots = container.find_elements(By.CSS_SELECTOR, '#root > div.jss13061 > div > div.jss13069 > div:nth-child(1) > div.jss13464.jss13468.jss13465')
#     slots = container.find_element(By.CSS_SELECTOR, "[data-testid='ProjectTimeSlot.IndividualProject green']")
#     for slot in slots:
#         print("slot " + slot)
#
#         time_text = slot.find_element(By.CSS_SELECTOR, '#root > div.jss13061 > div > div.jss13069 > div:nth-child(1) > div.jss13464.jss13472 > div.jss13466').text
#
#         description = slot.find_element(By.CSS_SELECTOR, '#root > div.jss13061 > div > div.jss13069 > div:nth-child(1) > div.jss13464.jss13472 > div.jss13467').text
#
#         # Проверяем, доступен ли слот для записи (например, по наличию определенного слова в описании)
#         if "Participant Peer Review" in description:
#             print(f"Доступный слот: Время: {time_text}, Описание: {description}")
#         else:
#             print(f"Недоступный слот: Время: {time_text}, Описание: {description}")