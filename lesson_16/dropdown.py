import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("http://the-internet.herokuapp.com/dropdown")

SELECT_LOCATOR = ('xpath', '//select[@id="dropdown"]')
DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))

time.sleep(2)

#DROPDOWN.select_by_visible_text("Option 1")
#DROPDOWN.select_by_value("2")
#DROPDOWN.select_by_index(1)  #0 element is the default one

ALL_OPTIONS = DROPDOWN.options
#print(ALL_OPTIONS)

for option in ALL_OPTIONS:
    time.sleep(1)
    if "Option 1" in option.text:
        print("Option 1 is available")
    DROPDOWN.select_by_visible_text(option.text)

for option in ALL_OPTIONS:
    time.sleep(1)
    DROPDOWN.select_by_index(ALL_OPTIONS.index(option))

for option in ALL_OPTIONS:
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value"))


time.sleep(2)