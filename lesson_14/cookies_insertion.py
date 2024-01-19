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

# LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
# PASSWORD_FIELD = ("xpath", "//input[@id='password']")
# SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")
#
# # Логинимся в аккаунт
# driver.get("https://www.freeconferencecall.com/en/us/login")
# driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
# driver.find_element(*PASSWORD_FIELD).send_keys("123")
# driver.find_element(*SUBMIT_BUTTON).click()

# pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/cookies.pkl", "wb"))

driver.delete_all_cookies()

cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)

driver.refresh()

time.sleep(5)