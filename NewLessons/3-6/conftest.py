import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language: e.g. --language=fr or --language=ru"
    )

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print(f"\nstart browser for test.. language={user_language}")

    options = Options()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": user_language}
    )


    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()
