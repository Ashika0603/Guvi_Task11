
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
    print("\nWebDriver closed.")

def login_url(setup):
    driver = setup
    driver.get("https://www.guvi.in/")
    driver.find_element(By.ID,"login-btn").click()
    print("navigated to Guvi login page")
    current_url =driver.current_url
    print("current URL",current_url)


def Uservalidation(setup):
    driver = setup
    driver.get("https://www.guvi.in/")
    driver.find_element(By.ID, "login-btn").click()
    print("navigated to Guvi login page")
    driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("ashikait06@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Positive@25")
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(5)
    print("Login success")


