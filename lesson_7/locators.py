import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/tracks")
print(driver.current_url, " - Is the URL - ", driver.title, " - is the Title")

time.sleep(3)

#Header
LOGO = driver.find_element("xpath", "//ul[@class='navbar-nav']")
THREE_BUTTONS = driver.find_elements("xpath", "//div[@class='nav_menu-links'] //a[contains(@class, 'nav-link')]")

LOGO.click()
time.sleep(3)

for button in THREE_BUTTONS:

    button.click()
    time.sleep(2)
    driver.back()
    time.sleep(1)

time.sleep(3)

#NavBar
NAVBAR = ('xpath', '//nav')
NAV_ELEMENTS = ('xpath', '//nav//li')
NAV_BUTTONS_RIGHT = ('xpath', '//div//button')


#Body
ALL_TRACKS_TAB = ("xpath", "//div[contains(@class, 'categories')]//a")
ALL_COURSES_CARDS = ('xpath', '//div[contains(@class, "card")]//div[@class="card-body"]')