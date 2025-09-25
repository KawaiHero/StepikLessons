from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Talgat')
    lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Gumirov')
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('GT@gmail.com')
    upload = browser.find_element(By.CSS_SELECTOR, '[id="file"]')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    upload.send_keys(file_path)

    btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()



finally:
    time.sleep(10)
    browser.quit()