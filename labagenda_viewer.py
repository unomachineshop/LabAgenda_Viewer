################################################################
# Author: Drake Bell
# Last Modified: 9/15/2018
# Description: This program provides an automated way to always
# show the 3D printing schedule to a display. It will 
# automatically log in, navigate to the desired page, and then 
# continually refresh said page showing the most up to date 
# schedule info.
################################################################
import time  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Interval to refresh webpage (seconds)
REFRESH = 10

# Web driver choice
driver = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe')
#driver = webdriver.Edge(executable_path='iedriver/MicrosoftWebDriver.exe')
#driver = webdriver.Firefox(executable_path='geckodriver/geckodriver.exe')

# Display window at maximum screen size
driver.maximize_window()

# Navigates to specified page, and waits for page load
driver.get('https://my.labagenda.com/index.php')

# Find email element and add appropiate email address
email = driver.find_element_by_id("email")
email.clear()
email.send_keys('XXXX@XXX.com')

# Find pass element and add appropiate password
password = driver.find_element_by_id("password")
password.clear()
password.send_keys('XXX')
login = driver.find_element_by_xpath('//*[@id="login-box"]/div[4]/button')

# Submit your credentials
login.click()

# Navigate to 'Machine Shop' page
driver.get('https://my.labagenda.com/schedule.php?sid=8642')


while(True):
	time.sleep(REFRESH)
	driver.refresh()

# Will close browser if enabled
#driver.close()