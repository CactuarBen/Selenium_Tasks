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

links = []
links.append("https://hyperskill.org/login")
links.append("https://www.google.com/")
links.append("https://www.yandex.ru/")

for i in range(len(links)):
    driver.get(links[i])
    driver.switch_to.new_window("tab")

windows = driver.window_handles
driver.switch_to.window(windows[0])
print(driver.title)
time.sleep(2)
button_one = driver.find_element('xpath', '//button[@type="submit"]')
button_one.click()

driver.switch_to.window(windows[1])
print(driver.title)
discard_button = driver.find_element('xpath', '/html/body/div[2]/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[1]/div')
discard_button.click()
button_two = driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]') #'(//input[@value="I\'m Feeling Lucky"])[2]')
button_two.click()

driver.switch_to.window(windows[2])
print(driver.title)
button_three = driver.find_element('xpath', '/html/body/div[2]/div[2]/div[7]/div/main/section[1]/div/aside/ul[1]/a[3]/li')
button_three.click()

time.sleep(3)

# driver.get("https://hyperskill.org/login")
# print(driver.title)
# button_one = driver.find_element('xpath', '//button[@type="submit"]')
# button_one.click()
# time.sleep(2)
#
# driver.switch_to.new_window("tab")
# driver.get("https://www.avito.ru/")
# print(driver.title)
# button_two = driver.find_element('xpath', '//div[contains(@class, "index-button-rtdlZ")]//span')
# button_two.click()
# time.sleep(2)
#
# driver.switch_to.new_window("tab")
# driver.get("https://www.ozon.ru/")
# print(driver.title)
# button_three = driver.find_element('xpath', '//span[text()="Sign in"]')
# button_three.click()
#
# time.sleep(3)