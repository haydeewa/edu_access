import os
from builtins import print, input, int, exit, ValueError

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import datetime
from datetime import timedelta
import time
import requests

def find_default_slot():

    # date_input = input("Input date for your slot (YYYY-MM-DD): ")
    #
    # try:
    #     input_date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
    #     day_of_week = input_date.weekday()  # Получение дня недели (0 - понедельник, 6 - воскресенье)
    #     print("Дата введена верно")
    # except ValueError:
    #     print("Ошибка: неверный формат даты")

    browser = webdriver.Chrome()
    url = 'https://edu.21-school.ru'
    browser.get(url)

    login(browser)

    action = ActionChains(browser)

    project = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/nav/section/div[1]/div[1]/div/div[4]')
    action.move_to_element(project).click().perform()

    in_project = browser.find_element(By.LINK_TEXT, 'Projects')
    in_project.click()

    time.sleep(2)

    sql = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/section/div/div[2]/div[2]/a[2]/div')
    sql.click()

    time.sleep(3)

    sql_projects = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/nav/div/div/section/div[2]/div/div/div[2]/div/a[1]')
    sql_projects.click()

    time.sleep(2)

    sql_day07 = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/main/div/div[2]/div/div/ul/a[9]/div')
    sql_day07.click()

    time.sleep(5)

    submit_for_rewiew = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/aside/div[1]/div/div/button')
    submit_for_rewiew.click()

    time.sleep(10)


    while True:
        try:
            # slot = browser.find_element(By.XPATH, f'//*[@id="root"]/div[4]/div/div[3]/div[{day_of_week + 1}]/div').find_element(By.CSS_SELECTOR, "[data-testid='ProjectTimeSlot.IndividualProject white']")
            # slot_time = slot.find_element(By.CSS_SELECTOR, '#root > div.jss15837 > div > div.jss15846 > div:nth-child(6) > div.jss16280.jss16296.jss16281 > div.jss16282')
            slot = browser.find_element(By.CSS_SELECTOR, "[data-testid='ProjectTimeSlot.IndividualProject white']")
            slot.click()
            time.sleep(2)
            subscribe = browser.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div[5]/div/div/div/div/div[4]/button')
            subscribe.click()
            print("Элемент появился на странице.")
            TOKEN = "6500910289:AAHru1ypiN9vapS74xwV_bPhw5CpOTB5MPE"
            chat_id = "332808756"
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text=Слот peer review найден"
            requests.get(url).json()
            break
        except:
            print("Элемент не найден. Обновляем страницу и ждем дальше.")
            browser.refresh()  # Обновляем страницу
            time.sleep(5)

def find_cr_slot():
    TOKEN = "6500910289:AAHru1ypiN9vapS74xwV_bPhw5CpOTB5MPE"
    chat_id = "332808756"


    browser = webdriver.Chrome()
    url = 'https://edu.21-school.ru'
    browser.get(url)

    login(browser)

    action = ActionChains(browser)

    project = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/nav/section/div[1]/div[1]/div/div[4]')
    action.move_to_element(project).click().perform()

    in_project = browser.find_element(By.LINK_TEXT, 'Projects')
    in_project.click()

    time.sleep(2)

    code_review = browser.find_element(By.LINK_TEXT, 'Code Review')
    code_review.click()

    time.sleep(2)


    while True:
        try:
            slot = browser.find_element(By.CSS_SELECTOR, "[data-testid='projectCard.container']")
            slot.click()
            time.sleep(2)
            select_the_slot = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/aside/div[1]/button')
            select_the_slot.click()
            time.sleep(3)


            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text=Слот code review найден"
            requests.get(url).json()
            print("Элемент появился на странице.")

            time.sleep(10000)
            # subscribe = browser.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div[5]/div/div/div/div/div[4]/button')
            # subscribe.click()
            break
        except:
            print("Элемент не найден. Обновляем страницу и ждем дальше.")
            browser.refresh()  # Обновляем страницу
            time.sleep(5)


def set_slot():
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

    login(browser)

    calendar = browser.find_element(By.LINK_TEXT, "Calendar")
    calendar.click()

    time.sleep(5)

    slot = browser.find_element(By.XPATH,
                                f'/html/body/div/div[4]/div/div[1]/div[{weekday_number + 2}]/div[{input_datetime.hour + 1}]')
    action = ActionChains(browser)
    action.move_to_element(slot).click().perform()

    start_of_slot = browser.find_element(By.XPATH,
                                         '//*[@id="root"]/div[4]/div/div[4]/div/div/div/div/div[4]/div[1]/div')
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

def login(browser):
    login = browser.find_element(By.CSS_SELECTOR, '#mui-1')
    login.send_keys('haydeewa@student.21-school.ru')

    password = browser.find_element(By.CSS_SELECTOR, '#mui-2')
    password.send_keys('ReforM2021!')

    enter = browser.find_element(By.CSS_SELECTOR, '#login > div.jss1 > div > div.jss4 > div > div > form > div.jss22 > button')
    enter.click()

    time.sleep(2)

def main():
    mode = int(input("Enter mode:\n1 ----- find default slot\n2 ----- find crp slot\n3 ----- set slot\n\nAny key to exit\n"))
    if mode == 1:
        find_default_slot()
    elif mode == 2:
        find_cr_slot()
    elif mode == 3:
        set_slot()
    else:
        exit()

if __name__ == "__main__":
    main()