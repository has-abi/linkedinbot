import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/login")


#Fill in a username
username = driver.find_element(By.ID, "username")
username.clear()
username.send_keys(os.environ.get("LINKEDIN_USERNAME"))

# Fill in password
username = driver.find_element(By.ID, "password")
username.clear()
username.send_keys(os.environ.get("LINKEDIN_PASSWORD"))

driver.find_element(By.XPATH, "//button[@data-litms-control-urn='login-submit']").click()
#driver.close()

WebDriverWait(driver, 4)
driver.find_element(By.XPATH, "//button[@aria-label='Click to start a search']").click()
linkedin_search = driver.find_element(By.XPATH, "//input[@aria-label='Search']")
linkedin_search.send_keys("Hassan Abida", Keys.ENTER)
time.sleep(3)
# Click the people button
driver.find_element(
    By.XPATH,
 "//button[text()='People']").click()


#result_elements = driver.find_elements(By.CLASS_NAME, "entity-result__item")
time.sleep(1)

# Find and click the profile of the first element
main = driver.find_element(By.ID, "main")

elems = main.find_elements(By.XPATH, "//div[@class='entity-result__item']")
elems[0].find_element(By.CLASS_NAME, "app-aware-link").click()
# for el in elems:
#     urls = el.find_elements(By.CLASS_NAME, "app-aware-link")
#     for u in urls:
#         print(u.get_attribute("href"))


time.sleep(3)
