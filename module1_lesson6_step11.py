from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
    print(input2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
    print(input3)
    input3.send_keys("IvPet@ya.ru")
    input4 = browser.find_element_by_xpath("//input[@placeholder='Input your phone:']")
    print(input4)
    input4.send_keys("88888888888")
    input5 = browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
    print(input5)
    input5.send_keys("Ufa")
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

