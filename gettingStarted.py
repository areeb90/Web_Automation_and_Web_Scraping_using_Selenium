from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
import time


driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)
time.sleep(5)  # Keep the window open for 5 seconds

assert "No results found." not in driver.page_source
driver.close()
