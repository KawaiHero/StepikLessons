from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "[class='trollface btn btn-primary']").click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text
    result = calc(x)

    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()




finally:
    time.sleep(10)
    browser.quit()