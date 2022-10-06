from selenium import webdriver

# open chrome webdriver
# note: there are different web drivers for different browsers (ie: firefoxDriver is for the FireFox browser.)
driver = webdriver.Chrome()

# send a request to the browser to get the url provided as a string argument
driver.get('https://www.google.com/')

# initialize searchField variable with xpath of search box div on google webpage
# note: to find the xpath, open google.com in chrome > inspect element > click area on webpage that you want python
# to interact with > right click tag > copy > xpath
searchField = driver.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

# input to search box string
searchField.send_keys('florida state university')

# submit search request
searchField.submit()