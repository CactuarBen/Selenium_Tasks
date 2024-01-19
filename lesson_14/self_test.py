import time
import os
import pickle

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/en/us/login")

driver.add_cookie({
    "name": "username",
    "value": "user123"
})

print(driver.get_cookie("username"))

print(driver.get_cookies())

driver.delete_cookie("split")

print(driver.get_cookies())