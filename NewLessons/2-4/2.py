from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 30, poll_frequency=1)

browser.get("https://suninjuly.github.io/explicit_wait2.html")


wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
browser.find_element(By.ID, "book").click()

x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text
result = calc(x)
browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(result)
browser.find_element(By.ID, 'solve').click()

time.sleep(5)