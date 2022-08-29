from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    add_to_basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert add_to_basket_button.is_displayed()