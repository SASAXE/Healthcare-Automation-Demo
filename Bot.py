import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

print("Starting...")

try:
    driver_path = "chromedriver.exe"

    local_service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=local_service)
    
    login_page_path = "file://" + os.path.abspath("login.html")

    print(f"Opening the 'Login page' at: {login_page_path}")

    driver.get(login_page_path)
    
    time.sleep(1) 

    print("Looking for login fields")
    
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    print("Typing in the login info")
    username_field.send_keys("my_username") #Insert your user name here
    time.sleep(0.5)
    password_field.send_keys("my_password") #Insert your password here
    time.sleep(0.5)
    
    print("Clicking the 'Log In' button")
    login_button.click()
    
    print("Inside Patient Status page")
    time.sleep(1)

    patient_id_field = driver.find_element(By.ID, "patient-id")
    status_button = driver.find_element(By.ID, "check-status-button")

    print("Typing the Patient ID")
    patient_id_field.send_keys("PATIENT_98765") #Insert the patient ID here
    time.sleep(0.5)
    
    print("Clicking 'Check Status'")
    status_button.click()
    
    time.sleep(1)

    print("Looking for the result")
    
    result_sign = driver.find_element(By.ID, "status-result")
    final_status = result_sign.text
    
    print(f"SUCCESS!: '{final_status}'")
    
except Exception as e:
    print(f"Error: {e}")

finally:
    print("Done. Closing the browser.")
    time.sleep(3)
    driver.quit()