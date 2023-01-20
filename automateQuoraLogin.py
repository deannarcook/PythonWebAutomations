# This code was created while practicing automate logging into Quora.
# Note 20221005: Code isn't working. need to find a way to automate recaptcha image test.

from time import sleep

from selenium import webdriver

# for repcaptcha
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# login info
UI_email = input('Enter your login email: ')
UI_password = input('Enter your password: ')


driver = webdriver.Chrome()

# open quora website
driver.get('https://www.quora.com/')

# xpath element for email field
emailField = driver.find_element('xpath','//*[@id="email"]')

# enter email address in email field
emailField.send_keys(UI_email)

# xpath element for password field
passwordField = driver.find_element('xpath','//*[@id="password"]')

# enter password in password field
passwordField.send_keys(UI_password)

sleep(10)

WebDriverWait(driver, 30).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()

sleep(3)

# xpath for login button
loginButton = driver.find_element('xpath','//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[5]/button')

# click login button
loginButton.click()
