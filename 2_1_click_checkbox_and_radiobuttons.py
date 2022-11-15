import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link="http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element(By.ID, "treasure")
    box_number = box.get_attribute("valuex")

    y = calc(box_number)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    robot_input = browser.find_element(By.ID,"robotCheckbox")
    robot_input.click()

    robot_rule = browser.find_element(By.ID,"robotsRule")
    robot_rule.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()

