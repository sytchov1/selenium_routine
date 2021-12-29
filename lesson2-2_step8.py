from selenium import webdriver
import time
import os


current_dir = os.path.abspath(os.path.dirname(__file__))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
try:
  browser.find_element_by_name("firstname").send_keys("my firstname")
  browser.find_element_by_name("lastname").send_keys("my lastname")
  browser.find_element_by_name("email").send_keys("myemail@gmail.com")

  filepath = os.path.join(current_dir, "new.txt")
  browser.find_element_by_id("file").send_keys(filepath)

  browser.find_element_by_css_selector("button[type=submit]").click()
finally:
  time.sleep(10)
  browser.quit()
