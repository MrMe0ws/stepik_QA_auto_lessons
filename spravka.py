#find_element(By.ID, value) — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
#find_element(By.CSS_SELECTOR, value) — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;
#find_element(By.XPATH, value) — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
# https://devhints.io/xpath справночник xPath

#find_element(By.NAME, value) — поиск по атрибуту name элемента;
#find_element(By.TAG_NAME, value) — поиск элемента по названию тега элемента;
#find_element(By.CLASS_NAME, value) — поиск по значению атрибута class;
#find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
#find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.

x_element.get_attribute("valuex") #возьми данные из атрибута, например в valuex="15" мы получим 15


#ERROR

#NoSuchElementException - нет такого вообще
#StaleElementReferenceException - был элемент да сплыл
#ElementNotVisibleException - видишь элемент? И я не вижу, а он есть.

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text

# Кейс №1
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://me0ws.ru/"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, ".header__navbar-img")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()



#Сценарий если кейс падает в ошибку, то код все равно закроется финл результатом закрытия

link = "https://me0ws.ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".header__navbar-img")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()