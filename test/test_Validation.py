import time

from selenium.common import NoSuchElementException
from Loginvalidation import *
from selenium.webdriver.common.by import By

def test_login_url(setup):
    driver = setup
    driver.get("https://www.guvi.in/")
    driver.find_element(By.ID, "login-btn").click()
    print("navigated to Guvi login page")
    current_url = driver.current_url
    print("current URL",current_url)
    if "https://www.guvi.in/sign-in/" == current_url:
        print("URL of the homepage validation is Successful")
    else:
        print("URL mismatch test failed")


def test_username_password_field(setup):

  try:
        driver = setup
        driver.get("https://www.guvi.in/")
        driver.find_element(By.ID, "login-btn").click()
        time.sleep(5)
        user_name = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        user_name_visible = user_name.is_displayed()
        user_name_enabled = user_name.is_enabled()
        print(f"Username box is visible: {user_name_visible}, Enabled: {user_name_enabled}")

        if user_name_visible and user_name_enabled:
            driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("ashikait06@gmail.com")
            print("Username input box validation passed.")
        else:
            print("Username input box validation failed.")

        password_visible = password.is_displayed()
        password_enabled = password.is_enabled()
        print(f"Password box is visible: {password_visible}, Enabled: {password_enabled}")

        if password_visible and password_enabled:
            driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Positive@25")
            print("Password input box validation passed.")
        else:
            print("Password input box validation failed.")

        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(5)

  except Exception as e:
        print(f"An error occurred: {e}")

def test_submit_button(setup):

  try:
        print("Validating Login Button")
        driver = setup
        driver.get("https://www.guvi.in/")
        driver.find_element(By.ID, "login-btn").click()
        time.sleep(5)
        print("navigated to Guvi login page")
        driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("ashikait06@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Positive@25")
        time.sleep(5)
        login_button = driver.find_element(By.LINK_TEXT, "Login")
        time.sleep(5)
        button_visible = login_button.is_displayed()
        button_enabled = login_button.is_enabled()
        if button_visible and button_enabled:
            login_button.click()
            time.sleep(5)
            print("Submit button validation passed.")
            print("Login success")
        else:
            print("Submit button validation failed.")
  except Exception as e:
        print(f"An error occurred: {e}")

def test_invalid_login(setup):
    try:
        driver = setup
        driver.get("https://www.guvi.in/")
        driver.find_element(By.ID, "login-btn").click()
        time.sleep(5)
        print("navigated to Guvi login page")
        driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("ashikait06@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Positive8@25")
        driver.find_element(By.LINK_TEXT, "Login").click()
        message = driver.find_element(By.XPATH,"//label[text()='Password']//following-sibling::div[@class='invalid-feedback']")
        time.sleep(5)
        if message.is_displayed():
           print("Invalid Username and Password")
    except Exception as e:
        print(f"An error occurred: {e}")

