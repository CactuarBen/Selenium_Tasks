import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Selenium")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# Locators
FORM_NAME_FIELD_LOCATOR = ('xpath', '//input[@id="RESULT_TextField-0"]')

#Main Script
driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to.frame("frame-one796456169")

driver.switch_to.default_content()

time.sleep(3)
driver.find_element(*FORM_NAME_FIELD_LOCATOR).send_keys("Aleksei")
time.sleep(3)
