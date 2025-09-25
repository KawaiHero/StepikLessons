from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    result = calc(x)
    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(result)
    btn = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()
    btn.click()



finally:
    time.sleep(10)
    browser.quit()