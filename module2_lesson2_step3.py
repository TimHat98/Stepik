from lib2to3.pytree import convert
from tkinter import Variable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum(x, y):
    return str(int(x) + int(y))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")    
    x = x_element.text
    y = y_element.text  
    z = sum(x, y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value('%s' % z)
    button = browser.find_element(By.CSS_SELECTOR,'button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()