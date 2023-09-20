from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(10)
    return chrome_browser

