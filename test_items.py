from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_cart_button(browser):
    browser.get(link)
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert button, 'Кнопка не обнаружена'
    time.sleep(2)