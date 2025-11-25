from Loginvalidation import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def teardown(driver):
    driver.quit()

url =login_validation()
current_url = url.login()
def test_login_url():
    if "https://www.guvi.in/sign-in/" == current_url:
        print("URL of the homepage validation is Successful")
    else:
        print("URL mismatch test failed")
    teardown(driver)

def test_username_password_field():

  try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.guvi.in/")
        driver.find_element(By.ID, "login-btn").click()
        user_name = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        is_user_name_visible = user_name.is_displayed()
        is_user_name_enabled = user_name.is_enabled()
        print(f"Username box is visible: {is_user_name_visible}, Enabled: {is_user_name_enabled}")

        if is_user_name_visible and is_user_name_enabled:
            print("Username input box validation passed.")
        else:
            print("Username input box validation failed.")

        is_password_visible = password.is_displayed()
        is_password_enabled = password.is_enabled()
        print(f"Password box is visible: {is_password_visible}, Enabled: {is_password_enabled}")

        if is_password_visible and is_password_enabled:
            print("Password input box validation passed.")
        else:
            print("Password input box validation failed.")

  except Exception as e:
        print(f"An error occurred: {e}")

  finally:
   # Close the browser
   driver.quit()
