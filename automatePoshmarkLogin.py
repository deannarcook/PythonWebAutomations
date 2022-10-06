from selenium import webdriver

# prompt user for username
UI_username = input('Enter your username: ')

# prompt user for password
UI_password = input('Enter your password: ')

# create Chrome webdriver
driver = webdriver.Chrome()

# open poshmark website
driver.get('https://poshmark.com/')

# find login button
logInButton = driver.find_element('xpath','//*[@id="app"]/header/nav/div/div/a[1]')

# click login button
logInButton.click()

# find username field
usernameField = driver.find_element('xpath','//*[@id="login_form_username_email"]')

# type username into field
usernameField.send_keys(UI_username)

# find password field
passwordField = driver.find_element('xpath', '//*[@id="login_form_password"]')

# type password into field
passwordField.send_keys(UI_password)

# find submit button
submitButton = driver.find_element('xpath','//*[@id="email-login-form"]/form/div[3]/button')

# click submit button
submitButton.click()