import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("https://testkru.com/Elements/Buttons")

LEFT_CLICK_BUTTON_LOCATOR = ('xpath', '//button[@id="leftClick"]')
DOUBLE_CLICK_BUTTON_LOCATOR = ('xpath', '//button[@id="doubleClick"]')
RIGHT_CLICK_BUTTON_LOCATOR = ('xpath', '//button[@id="rightClick"]')
HOVER_BUTTON_LOCATOR = ('xpath', '//button[@id="colorChangeOnHover"]')

left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
double_button = driver.find_element(*DOUBLE_CLICK_BUTTON_LOCATOR)
right_button = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)
hover_button = driver.find_element(*HOVER_BUTTON_LOCATOR)

action.click(left_button).perform()

time.sleep(3)

action.double_click(double_button).perform()

time.sleep(3)

action.context_click(right_button)

time.sleep(3)

#action.click(left_button).double_click(double_button).context_click(right_button)

action.click(left_button).pause(2).double_click(double_button).pause(2).context_click(right_button)

action.move_to_element(hover_button).perform()
