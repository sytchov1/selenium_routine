from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

num1 = int(browser.find_element_by_id("num1").text)
num2 = int(browser.find_element_by_id("num2").text)

browser.find_element_by_id("dropdown").click()
browser.find_element_by_css_selector(f"[value='{num1+num2}'").click()
browser.find_element_by_css_selector("button[type=submit]").click()
