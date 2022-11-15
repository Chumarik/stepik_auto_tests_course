import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link="http://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "input_value")
    x_num = int(num1.text)

    y = calc(x_num)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    robot_input = browser.find_element(By.ID,"robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_input)
    robot_input.click()

    robot_rule = browser.find_element(By.ID,"robotsRule")
    robot_rule.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
