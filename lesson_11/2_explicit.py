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

driver.get("https://demoqa.com/dynamic-properties")

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

BUTTON_ONE = wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON))
BUTTON_ONE.click()

time.sleep(3)

# ENABLE_IN_SECOND = ("xpath", "//button[@id='enableAfter']")
#
# BUTTON_TWO = wait.until(EC.element_to_be_clickable(ENABLE_IN_SECOND))
# BUTTON_TWO.click()