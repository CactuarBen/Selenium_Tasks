import time
import os
import pickle

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
#from fake_useragent import UserAgent

options = Options()
chrome_options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://amazon.com")

category_select = driver.find_element('xpath', '//img[@alt="Keyboards"]')
category_select.click()

product_select = driver.find_element('xpath', '(//a//span[contains(@class, "medium")])[2]')
product_select.click()

purchase = driver.find_element('xpath', '//input[@id="add-to-cart-button"]')
purchase.click()

cookies = driver.get_cookies()

pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/cookiesAmazon.pkl", "wb"))

driver.delete_all_cookies()

driver.refresh()

time.sleep(5)

cookies = pickle.load(open(os.getcwd()+"/cookies/cookiesAmazon.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

time.sleep(10)
