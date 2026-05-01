import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService


from selenium.webdriver.support.select import Select


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService('./tests/chromedriver'))
    return driver


def test_title_name(driver):
    driver.get("http://127.0.0.1:5000/")
    title = driver.title
    assert title == "Grade Marking System"