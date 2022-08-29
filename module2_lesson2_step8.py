from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'lastname')
    print(input2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, 'email')
    print(input3)
    input3.send_keys("IvPet@ya.ru")
    element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))     
    file_path = os.path.join(current_dir, '2.2file.txt')            
    element.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME,'button')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
