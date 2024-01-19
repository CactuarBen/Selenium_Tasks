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

#LOCATORS
FOR_BUSINESS_BUTTON_LOCATOR = ('xpath', '(//a[text()=" For Business "])')
START_FREE_BUTTON_LOCATOR = ('xpath', '(//a[text()="Start for Free"])')

driver.switch_to.new_window("tab") #write "window" for a new window
time.sleep(3)

# driver.get("https://hyperskill.org/tracks")
# time.sleep(5)
#
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
#
# driver.get("https://ya.ru")
# time.sleep(3)



# time.sleep(3)
#
# #print(driver.current_window_handle)
#
# driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
# time.sleep(3)
#
# tabs = driver.window_handles
# driver.switch_to.window(tabs[1])
#
# driver.find_element(*START_FREE_BUTTON_LOCATOR).click()
# time.sleep(3)

