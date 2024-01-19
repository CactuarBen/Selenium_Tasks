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

#driver.get_cookie("country_code")
cookies = driver.get_cookies()

# for cooka in cookies:
#     print(cooka)

driver.add_cookie({
    "name": "Example",
    "value": "Kukushka"
})

# print(driver.get_cookie("Example"))

before = driver.get_cookie("split")
#print(before)

driver.delete_cookie("split")
driver.delete_all_cookies()

driver.add_cookie({
    "name": "split",
    "value": "qwerty"
})

after = driver.get_cookies()
print(after)

