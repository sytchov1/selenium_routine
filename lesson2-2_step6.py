from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

try:
  x = int(browser.find_element_by_id("input_value").text)
  browser.find_element_by_id("answer").send_keys(calc(x))

  browser.find_element_by_id("robotCheckbox").click()
  rbutton = browser.find_element_by_id("robotsRule")
  browser.execute_script("return arguments[0].scrollIntoView(true);", rbutton)
  rbutton.click()

  browser.find_element_by_css_selector("button[type='submit']").click()
finally:
  time.sleep(10)
  browser.quit()