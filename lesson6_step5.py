from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #formula = str(math.ceil(math.pow(math.pi, math.e)*10000))
    #print(formula)
    #224592
    lin = browser.find_element(By.LINK_TEXT, "224592")
    lin.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(3)
    browser.quit()
