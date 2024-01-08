from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math
try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser,20).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
    cl = browser.find_element(By.ID, "book")
    cl.click()
    def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))

        # Ваш код, который заполняет обязательные поля

    x_element = browser.find_element(By.ID, 'input_value')
    check = x_element.text
    y = calc(check)
    b = browser.find_element(By.ID,'answer')
    b.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


        # Отправляем заполненную форму
    btn = browser.find_element(By.ID, "solve")
    btn.click()
    time.sleep(1)
    #C:\Users\user> environments\selenium_env\Scripts\activate.bat
    #python c:\Users\Administrator\selenium_course\wait.py
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
