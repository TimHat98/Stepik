from msilib.schema import RadioButton
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    input_for_answer = browser.find_element(By.ID, "answer")
    x = x_element.text
    y = calc(x)
    print(y)
    input_for_answer.send_keys(y)
    
    option1 = browser.find_element(By.ID,"robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID,"robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element(By.TAG_NAME,'button')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
