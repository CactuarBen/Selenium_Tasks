import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\downloads\whole"
}
chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")

upload_field = driver.find_element('xpath', '//input[@type="file"]')
upload_field.send_keys(f"{os.getcwd()}\downloads\Screenshot .png")

time.sleep(5)

driver.get("https://the-internet.herokuapp.com/download")

all_files = driver.find_elements('xpath', "//div[@class='example']//a")

for file in all_files:
    driver.execute_script("arguments[0].scrollIntoView();", file)
    file.click()


time.sleep(1)
