import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import os


# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)


# browser.execute_script("return arguments[0].scrollIntoView(true);", input)

input = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
values = ["Чонг", "Хан", "chong@mail.ru"]
inputs = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
for i in range(min(len(inputs), len(values))):
    inputs[i].clear()
    inputs[i].send_keys(values[i])

file = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
file.send_keys(file_path)
time.sleep(1.5)

button = browser.find_element(By. CSS_SELECTOR, '[type="submit"]')
button.click()

time.sleep(5)
browser.quit()
