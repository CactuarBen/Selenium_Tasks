import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://freeconferencecall.com/global/pl")

LOG_IN = driver.find_element('xpath', "//div[contains(@class, 'navbar-right')]/a")
#LOG_IN = driver.find_element('xpath', "//a[@id='login-desktop']").click()
LOG_IN.click()

email_field = driver.find_element("xpath", "//input[@id='login_email']")
email_field.send_keys("jesuschrist@ya.ru")

print(email_field.get_attribute("value"))

email_field.clear()

email_field.send_keys("testing...")
print(email_field.get_attribute("value"))

#time.sleep(2)
