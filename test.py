# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

# browser.get("http://suninjuly.github.io/cats.html")

# button = browser.find_element(By.ID, "button")
# button.click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
button.click()
