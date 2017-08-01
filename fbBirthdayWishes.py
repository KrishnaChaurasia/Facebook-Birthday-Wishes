# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 10:45:16 2017

@author: Krishna
"""

# Python script to log in to facebook and post birthday messages to friends' timeline on their birthdays!!
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time
 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

def page_loaded(driver):
	return driver.find_element_by_tag_name("body") != None
 
# Taking inputs from the console
print("Logging Details for Facebook:\n")
input_email_id = input("Enter Username/Email: ")
input_pwd = getpass.getpass()

# Initialize the PhantomJS
driver = webdriver.PhantomJS()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true'])
driver.implicitly_wait(20)
# Fetch the facebook login page
driver.get("https://www.facebook.com")
wait = WebDriverWait(driver, 20)
wait.until(page_loaded)

# Finding email and password fields and sending the keys
email = driver.find_element_by_id("email")
email.send_keys(input_email_id)
pwd = driver.find_element_by_id("pass")
pwd.send_keys(input_pwd)
pwd.send_keys(Keys.RETURN)

time.sleep(5)
driver.get("https://www.facebook.com/events/birthdays")
wait = WebDriverWait(driver, 20)
wait.until(page_loaded)

box_count = len(driver.find_elements_by_class_name("innerWrap"))

# Post on each of the friends' timeline 
for x in range(0, box_count):
	text_box = driver.find_element_by_tag_name('textarea')
	# The birthday message
	messgae = "Happy Birthday!!"
	text_box.send_keys(message)	
	time.sleep(5)
 
driver.close()