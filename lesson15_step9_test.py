import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# проверяем есть ли кнопка button.btn , ее нет, поэтому тест падает
def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()

#проверяем есть ли кнопка no_such_button , ее нет, поэтому тест ок
def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()
