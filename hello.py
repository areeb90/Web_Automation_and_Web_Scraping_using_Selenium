import os
from selenium import webdriver


os.environ['PATH'] += r"D:\DEV_Softwares\Chrome_Drivers\chrome-win32\chrome-win32\chromedriver.exe"

# Use double backslashes in the path

# Initialize the web driver
driver = webdriver.Chrome()
# Open the URL to be scraped and wait for it's load completion before moving on with the script execution
# Change this url according to your need, you
driver.get("https://www.google.com/search?q=python")
# can also pass the url as a command line argument
# #
# # # Find the element by it's id
# search_box = driver.find_element_by_id("search_form_input_homepage")
# # # Type in the search term
# search_box.send_keys("realpython")
# # # Find the element by it's id
# search_button = driver.find_element_by_id("search_button_homepage")
# # # Click the button
# search_button.click()
# # # Wait for the page to load
# driver.implicitly_wait(2)
# # # Find the element by it's class
# link = driver.find_element_by_class_name("result__a")
# # # Click the link
# link.click()
# # # Wait for the page to load
# driver.implicitly_wait(2)
# # # Find the element by it's class
# link = driver.find_element_by_class_name("btn-link")
# # # Click the link
# link.click()
# # # Wait for the page to load
# driver.implicitly_wait(2)
# # # Find the element by it's class
# link = driver.find_element_by_class_name("btn-link")
# # # Click the link
# link.click()
