import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker


link = "https://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
#browser.set_window_size(500, 1024)
browser.get(link)
time.sleep(1)

a = browser.find_element(By.ID, 'num1')
a = int(a.text)

b = browser.find_element(By.ID, 'num2')
b = int(b.text)

c = a + b
c = str(c)

select = browser.find_element(By.ID, 'dropdown')
select.send_keys(c)

sumbit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
sumbit.click()

time.sleep(2)
browser.quit()
