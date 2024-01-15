import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

driver.get("https://demoqa.com/dynamic-properties")

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

driver.find_element(*VISIBLE_AFTER_BUTTON).click()