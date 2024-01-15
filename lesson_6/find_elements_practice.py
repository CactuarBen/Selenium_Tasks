import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://wikipedia.com")
title = driver.title
print(title, "- is the title ")
time.sleep(2)

driver.find_element("id", "searchInput").send_keys("selenium")

time.sleep(3)

driver.find_element("class", "search-input-button").click()

time.sleep(5)