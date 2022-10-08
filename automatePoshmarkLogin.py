from selenium import webdriver
from time import sleep

def inputLoginInfo(prompt):
    userInput = input(prompt)
    return userInput

def launchChromeDefaultProfile(url):
    options = webdriver.ChromeOptions() # create object of ChromOptions class
    options.add_argument = {'/Users/deannacook/Library/Application Support/Google/Chrome/Default'} # add chrome profile path
    executablePath = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(executablePath,options=options)  # set chromedriver
    # executable path
    driver.maximize_window() # maximize url
    driver.get(url) # open url in chrome

    return driver

username = inputLoginInfo('Enter your username: ')

password = inputLoginInfo('Enter your password: ')

driver = launchChromeDefaultProfile('https://poshmark.com/')

# find login button
logInButton = driver.find_element('xpath','//*[@id="app"]/header/nav/div/div/a[1]')

# click login button
logInButton.click()

# find username field
usernameField = driver.find_element('xpath','//*[@id="login_form_username_email"]')

# type username into field
usernameField.send_keys(username)

# find password field
passwordField = driver.find_element('xpath', '//*[@id="login_form_password"]')

# type password into field
passwordField.send_keys(password)

# find submit button
submitButton = driver.find_element('xpath','//*[@id="email-login-form"]/form/div[3]/button')

# click submit button
submitButton.click()

sleep(60)

# find profile dropdown menu
profileDropDown = driver.find_element('xpath','//*[@id="app"]/header/nav[1]/div/ul/li[5]/div')

profileDropDown.click()

sleep(3)

myClosetOption = driver.find_element('xpath','//*[@id="app"]/header/nav[1]/div/ul/li[5]/div/div[2]/div/ul/li[1]/a')

myClosetOption.click()

shareClosetOption = driver.find_element('xpath','//*[@id="content"]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/ul/li[1]/div')

shareClosetOption.click()

sleep(5)

settingsButton = driver.find_element('xpath','//*[@id="content"]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div')

settingsButton.click()

shareToFollowersOption = driver.find_element('xpath','//*[@id="content"]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/i')

shareToFollowersOption.click()

#availableItemsRadioButton = driver.find_element('xpath','//*[@id="content"]/div/div[2]/div/div/nav/div/div[
# ''9]/div/div[2]/ul/li[2]/div/label/div')

#availableItemsRadioButton.click()