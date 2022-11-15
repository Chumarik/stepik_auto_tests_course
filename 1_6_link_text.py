import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link="http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    nambers=str(math.ceil(math.pow(math.pi, math.e)*10000))
    click_numbers=browser.find_element(By.LINK_TEXT,nambers)
    click_numbers.click()

    input1=browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2=browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3=browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4=browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR,'input[="Input your last name"]')
    button.click()

finally:
        time.sleep(30)
        browser.quit()
