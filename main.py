from time import sleep

from selenium import webdriver

# for repcaptcha
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

UI_email = input('Enter your login email: ')

UI_password = input('Enter your password: ')
# open quora website
driver = webdriver.Chrome()

# html tag element for email field
driver.get('https://www.quora.com/')

emailField = driver.find_element('xpath','//*[@id="email"]')
emailField.send_keys(UI_email)

passwordField = driver.find_element('xpath','//*[@id="password"]')
passwordField.send_keys(UI_password)

sleep(10)

WebDriverWait(driver, 30).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()

sleep(3)

loginButton = driver.find_element('xpath','//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[5]/button')

loginButton.click()
