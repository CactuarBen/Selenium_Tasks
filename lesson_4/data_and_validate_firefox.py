import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://vk.com/")

time.sleep(3)

url = driver.current_url
print(url, ": Current Url")
assert url == "https://vk.com/", "Wrong URL"

title = driver.title
print(title, " is the title")
assert title == "VK | Welcome!", "Wrong Title"

driver.get("https://ya.ru")
titleTwo = driver.title
print(titleTwo, "is the second page title")

driver.back()
title = driver.title
assert title == "VK | Welcome!"

driver.refresh()

urlNew = driver.current_url
print(urlNew, "New URL")

driver.forward()

urlLast = driver.current_url
print("Last URL: ", urlLast)




