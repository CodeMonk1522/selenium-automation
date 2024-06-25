from datetime import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


downlodPath = "Path to download it to the system."
username = 'connect@peoplehum.com'
password = 'Coviam@12345'


options = Options()
options.add_experimental_option("prefs", {"profile.default_content_settings.popups": 0,
                 "download.default_directory": downlodPath, 
                 "directory_upgrade": True})
options.add_experimental_option("detach", True)
# options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



print("Trying to load skype manager")
driver.get("https://manager.skype.com/reports")
print("Skype manager loaded")
time.sleep(5)


print("Waiting for Sign in or Create account btn")
driver.find_element(By.XPATH, "//span[contains(text(),'Sign in or Create account')]").click()
print("Clicked on sign in btn")
time.sleep(5)


print("Waiting for username input field")
driver.find_element(By.XPATH, "//input[@name='loginfmt']").send_keys(username)
print("Username entered")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='idSIButton9']").click()
print("Clicked on next btn")
time.sleep(5)


print("Waiting for password input field")
driver.find_element(By.XPATH, "//input[@name='passwd']").send_keys(password)
print("Password entered")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='idSIButton9']").click()
print("Clicked on sign in btn")
time.sleep(5)


print("Waiting for no btn")
driver.find_element(By.XPATH, "//*[@id='declineButton']").click()
print("Clicked no btn")
time.sleep(5)


# print("Selecting current day")
# today = datetime.now().strftime('%d')
# driver.find_element(By.CSS_SELECTOR, "#startDate").click()
# time.sleep(5)
# stDates = driver.find_elements(By.CSS_SELECTOR, ".ui-datepicker-calendar td")
# for d in stDates:
#     date1 = d.text
#     if date1 == today:
#         driver.execute_script("arguments[0].click();", d)
#         d.click()
#         time.sleep(5)
#         break
# print("Start date selected")
# driver.find_element(By.CSS_SELECTOR, "#endDate").click()
# time.sleep(5)
# endDates = driver.find_elements(By.CSS_SELECTOR, ".ui-datepicker-calendar td")
# print(stDates)
# for d in endDates:
#     date1 = d.text
#     if date1 == today:
#         driver.execute_script("arguments[0].click();", d)
#         d.click()
#         time.sleep(5)
#         break
# print("End date selected")


print("Selecting current day")
today = datetime.now().strftime('%d')
# driver.find_element(By.CSS_SELECTOR, "#startDate").click()
driver.find_element(By.XPATH, "//*[@id='startDate']").click()
time.sleep(5)
stDates = driver.find_elements(By.CSS_SELECTOR, ".ui-datepicker-today")
driver.execute_script("arguments[0].click();", stDates[0])
# stDates = driver.find_elements(By.CSS_SELECTOR, ".ui-datepicker-calendar td")
# for d in stDates:
#     date1 = d.text
#     print(d)
#     if date1 == today:
#         driver.execute_script("arguments[0].click();", d)
#         d.click()
#         time.sleep(5)
#         break
print("Start date selected")
# driver.find_element(By.CSS_SELECTOR, "#endDate").click()
driver.find_element(By.XPATH, "//*[@id='endDate']")
time.sleep(5)
endDates = driver.find_elements(By.CSS_SELECTOR, ".ui-datepicker-today")
driver.execute_script("arguments[0].click();", endDates[0])
# endDates = driver.find_elements(By.CSS_SELECTOR, ".ui-datepicker-calendar td")
# for d in endDates:
#     date1 = d.text
#     if date1 == today:
#         driver.execute_script("arguments[0].click();", d)
#         d.click()
#         time.sleep(5)
#         break
print("End date selected")


print("Waiting for go btn")
driver.find_element(By.CSS_SELECTOR, ".blue").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".blue").click()
time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, ".blue").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, ".blue").click()
# time.sleep(2)
print("Loaded data from current day")


print("Waiting for download btn")
driver.find_element(By.CSS_SELECTOR, "#downloadAllocationReports").click()
time.sleep(5)
print("Download btn clicked")


print("Waiting for orders")
checkBoxElement = driver.find_element(By.XPATH, "//*[@value ='orders']")
print(checkBoxElement.is_selected())
if checkBoxElement.is_selected():
    checkBoxElement.click()
time.sleep(2)
print("Waiting for allocation")
checkBoxElement = driver.find_element(By.XPATH, "//*[@value ='allocations']")
print(checkBoxElement.is_selected())
if checkBoxElement.is_selected():
    checkBoxElement.click()
print("Selected report")
time.sleep(2)


print("Waiting for generate btn")
driver.find_element(By.XPATH, "//button[contains(@name, 'generate')]").click()
print("Download button clicked")
time.sleep(10)

# driver.quit()
# print("Closed browser")

