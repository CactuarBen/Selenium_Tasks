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

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

#Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом
CHANGE_TEXT = driver.find_element('xpath', '//button[@id="populate-text"]')
TEXT_CHANGE = ('xpath', '//h2[@id="h2"]')

CHANGE_TEXT.click()
wait.until(EC.text_to_be_present_in_element(TEXT_CHANGE, "Selenium Webdriver"))

print("First test passed!")

#Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”
DISPLAY_BUTTON = driver.find_element('xpath', '//button[@id="display-other-button"]')
DISPLAY_BUTTON.click()

DISPLAY_BUTTON_HIDDEN = ('xpath', '//button[@id="hidden"]')
APPEARED_BUTTON_ONE = wait.until(EC.visibility_of_element_located(DISPLAY_BUTTON_HIDDEN))
APPEARED_BUTTON_ONE.click()
print("Second test passed!")

#Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”
ENABLE_BUTTON = driver.find_element('xpath', '//button[@id="enable-button"]')
SECOND_BUTTON = ("xpath", "//button[@id='disable']")

ENABLE_BUTTON.click()
wait.until(EC.element_to_be_clickable(SECOND_BUTTON)).click()
print("Third test passed!")
time.sleep(2)

#Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта
ALERT_BUTTON = driver.find_element('xpath', '//button[@id="alert"]')
ALERT_BUTTON.click()

wait.until(EC.alert_is_present())
print("Last test passed!!!")


#Extra
#CLICK_ME = driver.find_element('xpath', '//button[@id="disable"]')
#CLICK_ME_CHECKBOX = driver.find_element('xpath', '//input[@id="ch"]')