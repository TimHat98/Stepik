from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestsWeb(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()

    def execute_test(self, link):
        browser = webdriver.Chrome()
        input1 = self.browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("IvPet@ya.ru")
        input4 = self.browser.find_element_by_xpath("//input[@placeholder='Input your phone:']")
        input4.send_keys("88888888888")
        input5 = self.browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
        input5.send_keys("Ufa")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
              
        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text

    def tearDown(self):
        self.browser.quit()       
    
    def test1(self):
        link = "https://suninjuly.github.io/registration1.html"
        welcome_text = self.execute_test(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,  "User should successfully register")

    def test2(self):
        link = "https://suninjuly.github.io/registration2.html"
        welcome_text = self.execute_test(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,  "User should successfully register")

        

if __name__ == "__main__":
    unittest.main()