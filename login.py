from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# start chrome browser
driver = webdriver.Chrome()

# open login page
driver.get("https://practicetestautomation.com/practice-test-login/")


driver.maximize_window()

# enter username
driver.find_element(By.NAME,"username").send_keys("student")

# enter password
driver.find_element(By.NAME,"password").send_keys("Password123")

# click login
driver.find_element(By.ID,"submit").click()

time.sleep(500)

driver.quit()