import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker


def calc(x):
    return math.log(abs(12 * math.sin(float(x))))  # важно привести x к float


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "treasure")
x_checked = x_element.get_attribute("valuex")
x = x_checked
y = calc(x)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element(
    By.ID, 'answer')
input1.send_keys(y)

input2 = browser.find_element(
    By.CSS_SELECTOR, 'input[type="checkbox"]')
input2.click()

input3 = browser.find_element(
    By.CSS_SELECTOR, 'input[value="robots"]')
input3.click()

input4 = browser.find_element(
    By.CSS_SELECTOR, 'button[type="submit"]')
input4.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
