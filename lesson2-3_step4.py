from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

try:
  browser.find_element_by_css_selector("button[type=submit]").click()

  confirmView = browser.switch_to.alert
  confirmView.accept()

  x = int(browser.find_element_by_id("input_value").text)
  browser.find_element_by_id("answer").send_keys(calc(x))

  browser.find_element_by_css_selector("button[type=submit]").click()
finally:
  time.sleep(10)
  browser.quit()
