import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup_teardown():
    # Setupp
    service = Service()
    options = webdriver.ChromeOptions()
    chrome_options = Options()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    yield driver

    # Teardown
    time.sleep(5)
    driver.quit()

def test_login(setup_teardown):
    driver = setup_teardown

    url = "https://google.com"
    driver.get(url)

    time.sleep(5)
    driver.quit()