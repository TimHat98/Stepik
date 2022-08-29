from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = " http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    input_for_answer = browser.find_element(By.ID, "answer")
    x = x_element.text
    y = calc(x)
    print(y)
    input_for_answer.send_keys(y)
    
    option1 = browser.find_element(By.CSS_SELECTOR,"[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR,"[for='robotsRule']")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR,'button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()