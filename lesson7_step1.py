from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html?ruler=robots"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
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
