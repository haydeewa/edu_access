import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
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

action = ActionChains(browser)

project = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/nav/section/div[1]/div[1]/div/div[4]')
action.move_to_element(project).click().perform()


in_project = browser.find_element(By.LINK_TEXT, 'Projects')
in_project.click()

time.sleep(2)

sql = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/section/div/div[2]/div[2]/a[2]/div')
sql.click()

time.sleep(2)

sql_projects = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/nav/div/div/section/div[2]/div/div/div[2]/div/a[1]')
sql_projects.click()

time.sleep(2)

sql_day05 = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/main/div/div[2]/div/div/ul/a[7]/div')
sql_day05.click()

time.sleep(5)

submit_for_rewiew = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/aside/div[1]/div/div/button')
submit_for_rewiew.click()

time.sleep(10)

# Находим все элементы с классом "jss3126", предполагая, что это контейнеры для слотов
# slot_containers = browser.find_elements(By.CLASS_NAME, 'jss3188')
# 3200
# //*[@id="root"]/div[4]/div/div[3]/div[1]
# //*[@id="root"]/div[4]/div/div[3]/div[2]
# //*[@id="root"]/div[4]/div/div[2]/div[2]
# //*[@id="root"]/div[4]/div/div[2]/div[3]
# //*[@id="root"]/div[4]/div/div[2]/div[7]

#root > div.jss13061 > div > div.jss13069 > div:nth-child(1) > div.jss13464.jss13472
#root > div.jss13061 > div > div.jss13069 > div:nth-child(1) > div.jss13464.jss13468.jss13465

xpath = []

for i in range(1, 8):
    xpath.append('//*[@id="root"]/div[4]/div/div[2]/div[' + str(i) + ']')

slot_containers = []

for path in xpath:
    print(path)
    slot = browser.find_element(By.XPATH, path)
    slot_containers.append(slot)


for container in slot_containers:
    print("tut")

    # slots = container.find_elements(By.CSS_SELECTOR, '#root > div.jss13061 > div > div.jss13069 > div:nth-child(1) > div.jss13464.jss13468.jss13465')
    slots = container.find_element(By.CSS_SELECTOR, '#root > div.jss13061 > div > div.jss13069 > div:nth-child(1) > div.jss13464.jss13468.jss13465')
    for slot in slots:
        print("slot " + slot)

        time_text = slot.find_element(By.CSS_SELECTOR, '#root > div.jss13061 > div > div.jss13069 > div:nth-child(1) > div.jss13464.jss13472 > div.jss13466').text

        description = slot.find_element(By.CSS_SELECTOR, '#root > div.jss13061 > div > div.jss13069 > div:nth-child(1) > div.jss13464.jss13472 > div.jss13467').text

        # Проверяем, доступен ли слот для записи (например, по наличию определенного слова в описании)
        if "Participant Peer Review" in description:
            print(f"Доступный слот: Время: {time_text}, Описание: {description}")
        else:
            print(f"Недоступный слот: Время: {time_text}, Описание: {description}")

# code_review = browser.find_element(By.LINK_TEXT, 'Code Review')
# code_review.click()
#
# time.sleep(2)
#
# initial_page_source = browser.page_source
# with open("page_new.html", "w", encoding="utf-8") as file:
#     file.write(initial_page_source)
#     print("code is write")
#
# wait = WebDriverWait(browser, 10)
# while True:
#     browser.refresh()  # Обновляем страницу
#     time.sleep(2)
#
#     try:
#         element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div/section/div/div[1]/div/div/div/div[2]/a/div')))
#         print("Элемент появился на странице.")
#         break
#     except:
#         print("Элемент не найден. Обновляем страницу и ждем дальше.")

time.sleep(5)

# //*[@id="menu-"]/div[3]/ul/li[1]

