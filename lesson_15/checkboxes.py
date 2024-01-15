import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://the-internet.herokuapp.com/checkboxes")

CHECKBOX_1 = ('xpath', '(//input[@type="checkbox"])[1]')
# print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))
# #print(driver.find_element(*CHECKBOX_1).is_selected())
# driver.find_element(*CHECKBOX_1).click()
# print(driver.find_element(*CHECKBOX_1).get_attribute("checked"))
# #print(driver.find_element(*CHECKBOX_1).is_selected())
# time.sleep(2)