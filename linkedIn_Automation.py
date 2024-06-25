from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
#from bs4 import BeautifulSoup

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
time.sleep(2)

#********** LOG IN *************

username = driver.find_element(by=By.XPATH, value="//input[@name='session_key']")
password = driver.find_element(by=By.XPATH, value="//input[@name='session_password']")

username.send_keys('username') #Enter your username
password.send_keys('password') #Enter your password

time.sleep(2)

submit = driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()

#***************** ADD CONTACTS ***********************
import random

n_pages = 7



for n in range(2, n_pages + 1):

    driver.get("https://www.linkedin.com/search/results/people/?keywords=human%20resources&network=%5B%22F%22%2C%22S%22%5D&origin=FACETED_SEARCH&page=" + str(n))
    time.sleep(2)
    


    all_buttons = driver.find_elements(By.TAG_NAME, value="button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
    



    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(3.5)

        add_note = driver.find_element(by=By.XPATH, value="//button[@aria-label='Add a note']")
        driver.execute_script("arguments[0].click();", add_note)
        customMessage = "Hello, With the holiday season around the corner, it’s the most wonderful chaotic time of the year for HR. Take our fun quiz to find out which HR reindeer you are! https://s.peoplehum.com/ew5v3"

        message = driver.find_element(By.ID, 'custom-message')
        message.send_keys(customMessage)
        time.sleep(4)
        

        send = driver.find_element(by=By.XPATH, value="//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
        time.sleep(3.7644)
        close = driver.find_element(by=By.XPATH, value="//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)
        time.sleep(4.232)