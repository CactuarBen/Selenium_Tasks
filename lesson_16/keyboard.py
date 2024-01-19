import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

#driver.get("http://the-internet.herokuapp.com/key_presses")
driver.get("http://demoqa.com/select-menu")

SELECT_LOCATOR = ("xpath", "//input[@#id='react-select-3-input']")

#KEYBOARD_INPUT = ('xpath', '//input[@id="target"]')

#driver.find_element(*KEYBOARD_INPUT).send_keys("SDKFJ:KSBF:E")
#driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.ENTER)

driver.find_element(*SELECT_LOCATOR).send_keys("Ms.")
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)

time.sleep(5)