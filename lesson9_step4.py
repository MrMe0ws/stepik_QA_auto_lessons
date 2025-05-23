from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# Подробнее про другие функции https://stepik.org/lesson/181384/step/7?unit=156009
button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, "verify")))
button.click()
message = browser.find_element(By.ID, "verify_message")

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
    EC.element_to_be_clickable((By.ID, "verify"))
)

assert "successful" in message.text

browser.quit()