from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    first.send_keys("John")

    last = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    last.send_keys("Dow")

    e_mail = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    e_mail.send_keys("jdow@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()