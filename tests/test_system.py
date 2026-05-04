import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService


from selenium.webdriver.support.select import Select
from selenium.webdriver.support.color import Color


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService('./tests/chromedriver'))
    return driver

def test_title_name(driver):
    driver.get("http://127.0.0.1:5000/")
    title = driver.title
    assert title == "Grade Marking System"

def test_h1(driver):
    driver.get("http://127.0.0.1:5000/")
    h1 = driver.find_element(By.ID, "h1")
    assert h1.text == "Grade Marking System"

def test_h2(driver):
    driver.get("http://127.0.0.1:5000/")
    h2 = driver.find_element(By.ID, "h2")
    assert h2.text == "Load Student File"

def test_file_name(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("students.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()

def test_table_r1(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("students.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()

    fname = driver.find_element(By.XPATH,"//table/tbody/tr[1]/td[1]").text
    score = driver.find_element(By.XPATH,"//table/tbody/tr[1]/td[2]").text
    grade = driver.find_element(By.XPATH,"//table/tbody/tr[1]/td[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"grade-1").value_of_css_property("background-color"))

    assert fname == "Evan"
    assert score == "99.0"
    assert grade == "1"
    assert bgcolour.rgb == "rgb(255, 215, 0)"