from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element(By.ID,"treasure")
    chest_valuex = chest.get_attribute("valuex")
    input_for_answer = browser.find_element(By.ID, "answer")
    x = chest_valuex
    y = calc(x)
    print(y)
    input_for_answer.send_keys(y)
    
    option1 = browser.find_element(By.CSS_SELECTOR,"[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR,"[id='robotsRule']")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR,'button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()