import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

# url = driver.current_url
# print("URL webpage: ", driver.current_url)
#
# current_title = driver.title
# print("Title webpage: ", driver.title)
#
# assert url == "https://www.wikipedia.org/", "URL Error, wrong webpage"
# assert current_title == "Wikipedia", "Title Error, wrong URL"

print(driver.page_source)

time.sleep(3)