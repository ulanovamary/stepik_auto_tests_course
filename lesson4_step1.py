from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome()
    browser.implicitly_wait(12)
    browser.get(link)

    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    if button == True:
        btn = browser.find_element_by_id('book')

        btn.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


        # Ваш код, который берет х и считает значение функции
    input_value = browser.find_element(By.ID, "input_value")

    x = input_value.text

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

        # ждем загрузки страницы
        # time.sleep(1)

        # нажать кнопку
    #browser.switch_to.window(new_window)
    button = browser.find_element_by_css_selector("body > form > div > div > button")
    button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        # time.sleep(1)
finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
        # закрываем браузер после всех манипуляций
    browser.quit()