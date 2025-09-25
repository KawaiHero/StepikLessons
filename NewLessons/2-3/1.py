from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']").click()
    browser.switch_to.alert.accept()

    x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text
    result = calc(x)

    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()




finally:
    time.sleep(10)
    browser.quit()