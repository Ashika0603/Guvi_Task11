
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time

class login_validation:

 def login(self):
         global driver
         driver = webdriver.Chrome()
         driver.maximize_window()
         driver.get("https://www.guvi.in/")
         driver.find_element(By.ID,"login-btn").click()
         print("navigated to Guvi login page")
         current_url = driver.current_url
         return current_url

 def user_validation(self):
         global driver
         driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("ashikait06@gmail.com")
         driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("Positive@25")
         time.sleep(5)
         driver.find_element(By.LINK_TEXT,"Login").click()
         time.sleep(5)
         print("Login success")
         driver.quit()
         sys.exit()

login_val = login_validation()
login_val.login()
login_val.user_validation()