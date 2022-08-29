from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.XPATH,'//button[text()="I want to go on a magical journey!"]')
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element(By.ID, "input_value")
    input_for_answer = browser.find_element(By.ID, "answer")
    x = x_element.text
    y = calc(x)
    print(y)
    input_for_answer.send_keys(y)
    
    button2 = browser.find_element(By.XPATH,'//button[text()="Submit"]')
    button2.click()
    

finally:
    time.sleep(30)
    browser.quit()