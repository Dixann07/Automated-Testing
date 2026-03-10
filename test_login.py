from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Get the path to index.html
file_path = "file://" + os.path.abspath("index.html")

# Setup Chrome driver
options = webdriver.ChromeOptions()
# options.add_argument('--headless') # Uncomment to run without a browser window
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def test_login_success():
    print("Testing successful login...")
    driver.get(file_path)
    
    # Locate elements
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.ID, "loginButton")
    
    # Enter credentials
    username_input.send_keys("admin")
    password_input.send_keys("password123")
    
    # Submit form
    submit_button.click()
    
    # Verify result
    time.sleep(1) # Small delay to allow JS to run
    message = driver.find_element(By.ID, "message").text
    print(f"Result message: {message}")
    assert "Login Successful!" in message
    print("Success: Test passed!")

def test_login_failure():
    print("\nTesting failed login...")
    driver.refresh()
    
    # Locate elements
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.ID, "loginButton")
    
    # Enter wrong credentials
    username_input.send_keys("wrong_user")
    password_input.send_keys("wrong_pass")
    
    # Submit form
    submit_button.click()
    
    # Verify result
    time.sleep(1)
    message = driver.find_element(By.ID, "message").text
    print(f"Result message: {message}")
    assert "Invalid credentials" in message
    print("Success: Test passed!")

try:
    test_login_success()
    test_login_failure()
finally:
    print("\nClosing browser...")
    time.sleep(2)
    driver.quit()
