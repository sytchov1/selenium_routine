from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
  book_button = browser.find_element(By.ID, "book")
  WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
  book_button.click()

  x = int(browser.find_element_by_id("input_value").text)
  browser.find_element_by_id("answer").send_keys(calc(x))
  browser.find_element_by_css_selector("button[type=submit]").click()
finally:
  time.sleep(10)
  browser.quit()
