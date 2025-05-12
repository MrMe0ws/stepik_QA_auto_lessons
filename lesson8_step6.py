import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker


def calc(x):
    return math.log(abs(12 * math.sin(float(x))))  # важно привести x к float

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
number = browser.find_element(By.ID, 'input_value')
x = int(number.text)
y = calc(x)
input = browser.find_element(By.CSS_SELECTOR, '[type="text"]')
time.sleep(1.5)
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(y)

checkbox = browser.find_element(By. CSS_SELECTOR, '[type="checkbox"]')
checkbox.click()

robot = browser.find_element(By. CSS_SELECTOR, '[value="robots"]')
robot.click()

button = browser.find_element(By. CSS_SELECTOR, '[type="submit"]')
button.click()

time.sleep(5)
browser.quit()






