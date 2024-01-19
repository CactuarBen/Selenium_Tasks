import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("https://seiyria.com/bootstrap-slider")

driver.execute_script("alert('Hello')")

EX_2_LOCATOR = ('xpath','//h3[text()="Example 2: "]')
EX_2 = driver.find_element(*EX_2_LOCATOR)

action.scroll_to_element()

time.sleep(5)