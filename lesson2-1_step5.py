from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x = browser.find_element_by_id("input_value").text
answer_field = browser.find_element_by_id("answer")
answer_field.send_keys(calc(x))

browser.find_element_by_css_selector("[for=robotCheckbox]").click()
browser.find_element_by_css_selector("[for=robotsRule]").click()
browser.find_element_by_css_selector("button[type=submit]").click()
