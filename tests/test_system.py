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

def test_student_file(driver):
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
    time.sleep(1)

    fname = driver.find_element(By.XPATH,"//table/tbody/tr[1]/td[1]").text
    score = driver.find_element(By.XPATH,"//table/tbody/tr[1]/td[2]").text
    grade = driver.find_element(By.XPATH,"//table/tbody/tr[1]/td[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"grade-1").value_of_css_property("background-color"))

    assert fname == "Evan"
    assert score == "99.0"
    assert grade == "1"
    assert bgcolour.rgb == "rgb(255, 215, 0)"

def test_results_file(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("results.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()

def test_results_thead(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("results.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()
    time.sleep(1)

    thead1 = driver.find_element(By.XPATH,"//table/thead/tr[1]/th[1]").text
    thead2 = driver.find_element(By.XPATH,"//table/thead/tr[1]/th[2]").text
    thead3 = driver.find_element(By.XPATH,"//table/thead/tr[1]/th[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"start").value_of_css_property("background-color"))

    assert thead1 == "Name"
    assert thead2 == "Score"
    assert thead3 == "Grade"
    assert bgcolour.rgb == "rgb(211, 211, 211)"

def test_results_r1(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("results.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()
    time.sleep(1)

    fname = driver.find_element(By.XPATH,"//table/tbody/tr[1]/td[1]").text
    score = driver.find_element(By.XPATH,"//table/tbody/tr[1]/td[2]").text
    grade = driver.find_element(By.XPATH,"//table/tbody/tr[1]/td[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"grade-1").value_of_css_property("background-color"))

    assert fname == "John"
    assert score == "71.0"
    assert grade == "1"
    assert bgcolour.rgb == "rgb(255, 215, 0)"

def test_results_r2(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("results.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()
    time.sleep(1)

    fname = driver.find_element(By.XPATH,"//table/tbody/tr[2]/td[1]").text
    score = driver.find_element(By.XPATH,"//table/tbody/tr[2]/td[2]").text
    grade = driver.find_element(By.XPATH,"//table/tbody/tr[2]/td[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"grade-1").value_of_css_property("background-color"))

    assert fname == "Paul"
    assert score == "70.0"
    assert grade == "1"
    assert bgcolour.rgb == "rgb(255, 215, 0)"

def test_results_r3(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("results.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()
    time.sleep(1)

    fname = driver.find_element(By.XPATH,"//table/tbody/tr[3]/td[1]").text
    score = driver.find_element(By.XPATH,"//table/tbody/tr[3]/td[2]").text
    grade = driver.find_element(By.XPATH,"//table/tbody/tr[3]/td[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"grade-2_1").value_of_css_property("background-color"))

    assert fname == "George"
    assert score == "69.0"
    assert grade == "2_1"
    assert bgcolour.rgb == "rgb(192, 192, 192)"

def test_results_r5(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("results.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()
    time.sleep(1)

    fname = driver.find_element(By.XPATH,"//table/tbody/tr[5]/td[1]").text
    score = driver.find_element(By.XPATH,"//table/tbody/tr[5]/td[2]").text
    grade = driver.find_element(By.XPATH,"//table/tbody/tr[5]/td[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"grade-2_2").value_of_css_property("background-color"))

    assert fname == "Bob"
    assert score == "59.0"
    assert grade == "2_2"
    assert bgcolour.hex == "#cd7f32"

def test_results_r8(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("results.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()
    time.sleep(1)

    fname = driver.find_element(By.XPATH,"//table/tbody/tr[8]/td[1]").text
    score = driver.find_element(By.XPATH,"//table/tbody/tr[8]/td[2]").text
    grade = driver.find_element(By.XPATH,"//table/tbody/tr[8]/td[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"grade-Pass").value_of_css_property("background-color"))

    assert fname == "Bill"
    assert score == "40.0"
    assert grade == "Pass"
    assert bgcolour.rgb == "rgb(0, 128, 0)"

def test_results_r9(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("results.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()
    time.sleep(1)

    fname = driver.find_element(By.XPATH,"//table/tbody/tr[9]/td[1]").text
    score = driver.find_element(By.XPATH,"//table/tbody/tr[9]/td[2]").text
    grade = driver.find_element(By.XPATH,"//table/tbody/tr[9]/td[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"grade-Fail").value_of_css_property("background-color"))

    assert fname == "Rob"
    assert score == "39.0"
    assert grade == "Fail"
    assert bgcolour.rgb == "rgb(255, 0, 0)"

def test_results_r10(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("results.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()
    time.sleep(1)

    fname = driver.find_element(By.XPATH,"//table/tbody/tr[10]/td[1]").text
    score = driver.find_element(By.XPATH,"//table/tbody/tr[10]/td[2]").text
    grade = driver.find_element(By.XPATH,"//table/tbody/tr[10]/td[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"grade--1").value_of_css_property("background-color"))

    assert fname == "Score must be between 0 and 100."
    assert score == "-1"
    assert grade == "-1"
    assert bgcolour.rgb == "rgb(255, 192, 203)"

def test_results_r11(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("results.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()
    time.sleep(1)

    fname = driver.find_element(By.XPATH,"//table/tbody/tr[11]/td[1]").text
    score = driver.find_element(By.XPATH,"//table/tbody/tr[11]/td[2]").text
    grade = driver.find_element(By.XPATH,"//table/tbody/tr[11]/td[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"grade--1").value_of_css_property("background-color"))

    assert fname == "could not convert string to float: 'twenty'"
    assert score == "-1"
    assert grade == "-1"
    assert bgcolour.rgb == "rgb(255, 192, 203)"

def test_results_r12(driver):
    driver.get("http://127.0.0.1:5000/")
    filename = driver.find_element(By.ID, "filename")
    filename.send_keys("results.txt")
    button = driver.find_element(By.ID, "submit-btn")
    button.click()
    time.sleep(1)

    fname = driver.find_element(By.XPATH,"//table/tbody/tr[12]/td[1]").text
    score = driver.find_element(By.XPATH,"//table/tbody/tr[12]/td[2]").text
    grade = driver.find_element(By.XPATH,"//table/tbody/tr[12]/td[3]").text
    bgcolour = Color.from_string(driver.find_element(By.CLASS_NAME,"grade--1").value_of_css_property("background-color"))

    assert fname == "Name must be a non-empty string."
    assert score == "-1"
    assert grade == "-1"
    assert bgcolour.rgb == "rgb(255, 192, 203)"

