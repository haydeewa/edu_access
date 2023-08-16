import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
import datetime
from datetime import timedelta
import time

os.chdir(r'/Users/haydeewa/')
os.getcwd()

date_input = input("Input date for your slot (YYYY-MM-DD): ")
time_input = input("Input time for your slot (HH:MM): ")
slot_duration = int(input("Input duration of the slot (MM): "))


try:
    input_datetime = datetime.datetime.strptime(f"{date_input} {time_input}", "%Y-%m-%d %H:%M")
    duration = timedelta(minutes=slot_duration)
except ValueError:
    print("Ошибка: неверный формат даты или времени")
    exit()

green_time = (input_datetime - timedelta(hours=3)).strftime("%H:%M:%S")
green_time_with_duration = (input_datetime - timedelta(hours=3) + duration).strftime("%H:%M:%S")

current_datetime = datetime.datetime.now()

if input_datetime < current_datetime:
    print("Ошибка: введенная дата и время меньше текущих")
    exit()

if slot_duration % 15 != 0:
    print("Error: duration is not a multiple of 15")
    exit()

print("Введенная дата и время корректны.")

weekday_number = input_datetime.weekday()


browser = webdriver.Chrome()
url = 'https://edu.21-school.ru'
browser.get(url)

login = browser.find_element(By.CSS_SELECTOR, '#mui-1')
login.send_keys('haydeewa@student.21-school.ru')

password = browser.find_element(By.CSS_SELECTOR, '#mui-2')
password.send_keys('ReforM2021!')

enter = browser.find_element(By.CSS_SELECTOR, '#login > div.jss1 > div > div.jss4 > div > div > form > div.jss22 > button')
enter.click()

time.sleep(5)


calendar = browser.find_element(By.LINK_TEXT, "Calendar")
calendar.click()

time.sleep(5)

slot = browser.find_element(By.XPATH, f'/html/body/div/div[4]/div/div[1]/div[{weekday_number + 2}]/div[{input_datetime.hour}]')
action = ActionChains(browser)
action.move_to_element(slot).click().perform()

start_of_slot = browser.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div[4]/div/div/div/div/div[4]/div[1]/div')
start_of_slot.click()

time.sleep(2)

time_of_start = browser.find_element(By.CSS_SELECTOR, f"[data-value='{date_input}T{green_time}.000Z']")
time_of_start.click()




end_of_slot = browser.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div[4]/div/div/div/div/div[4]/div[2]/div')
end_of_slot.click()

time_of_end = browser.find_element(By.CSS_SELECTOR, f"[data-value='{date_input}T{green_time_with_duration}.000Z']")
time_of_end.click()


save_button = browser.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div[4]/div/div/div/div/div[5]/button')
action.move_to_element(save_button).click().perform()
action.move_to_element(save_button).click().perform()

time.sleep(15)

