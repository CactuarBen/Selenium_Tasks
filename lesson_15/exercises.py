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

driver.get("https://demoqa.com/selectable")

grid_button = driver.find_element('xpath', '//a[@id="demo-tab-grid"]')
grid_button_class = grid_button.get_attribute("class")
new_class = grid_button_class + " active "
driver.execute_script("arguments[0].setAttribute('class', arguments[1]);", grid_button, new_class)
grid_button.click()

gridRowOne = driver.find_element('xpath', '//div[@id="gridContainer"]/div[@id="row1"]')
gridRowOne = driver.find_element('xpath', '//div[@id="gridContainer"]/div[@id="row1"]')
gridRowOne = driver.find_element('xpath', '//div[@id="gridContainer"]/div[@id="row1"]')

squares = driver.find_elements('xpath', '//div[@id="gridContainer"]//li[contains(@class, "list-group-item")]')

for square in squares:
    square.click();

for square in squares:
    print(square.get_attribute("class"))

time.sleep(3)

for square in squares:
    square.click();

for square in squares:
    print(square.get_attribute("class"))

time.sleep(3)