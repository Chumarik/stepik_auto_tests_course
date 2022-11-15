from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    first_name = browser.find_element(By.XPATH, './/input[@placeholder="Input your first name"]')
    first_name.send_keys("Akaky")
    
    last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
    last_name.send_keys("Poopkin")
    
    email = browser.find_element(By.CSS_SELECTOR, '.third')
    email.send_keys("prosto@mail.ru")
    
    phone = browser.find_element(By.XPATH, './/input[@placeholder="Input your phone:"]')
    phone.send_keys(88005553555)
    
    address = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your address:"]')
    address.send_keys()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
