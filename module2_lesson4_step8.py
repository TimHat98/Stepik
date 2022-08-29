from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    button1 = browser.find_element(By.ID, "book")
    price100 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button1.click()

    x_element = browser.find_element(By.ID, "input_value")
    input_for_answer = browser.find_element(By.ID, "answer")
    x = x_element.text
    y = calc(x)
    print(y)
    input_for_answer.send_keys(y)
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(30)
    browser.quit()    
