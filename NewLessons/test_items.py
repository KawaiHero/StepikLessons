from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_basket(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button.is_displayed()
    print("\nThere is button on the page")