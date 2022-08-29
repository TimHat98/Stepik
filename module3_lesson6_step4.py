import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc_result():
    answer = math.log(int(time.time()))
    return answer

@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1",
                                "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", 
                                "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])

def test_that_answer_is_correct(browser, url):
    browser.get(url)
    browser.implicitly_wait(10)
    field_for_answer = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ember-text-area"))
    )
    answer = calc_result()
    print(answer)
    field_for_answer = browser.find_element(By.CLASS_NAME, "ember-text-area")
    field_for_answer.send_keys(answer)
    submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
    submit_button.click()
    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    print(message)
    print(message.text)
    assert "Correct!" in message.text