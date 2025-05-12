from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# Подробнее про другие функции https://stepik.org/lesson/181384/step/7?unit=156009
button = browser.find_element(By.ID, 'book')
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
    (By.ID, "price"), "100"))
button.click()

y = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
x = int(y.text)


def calc(x):
    return math.log(abs(12 * math.sin(float(x))))  # важно привести x к float

a = calc(x)

input = browser.find_element(By.CSS_SELECTOR, '[type="text"]')
input.send_keys(a)

submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
submit.click()

time.sleep(5)
browser.quit()
