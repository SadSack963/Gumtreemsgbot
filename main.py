import useragent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from random import randint, choice
import requests
from fake_useragent import UserAgent
import os
from webdrivermanager.chrome import ChromeDriverManager
import selenium.common.exceptions as exceptions


USERNAME = "username"
PASSWORD = "password"

# User Agent randomly change

ua = UserAgent()
random_header = ua.random

# headless Selenium
options = Options()
options.headless = False
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(f'user-agent={random_header}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

chrome_driver_path = "E:/Python/WebDriver/chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

url = "https://www.gumtree.com.au/"
login_url = "https://www.gumtree.com.au/t-login-form.html"

driver.get(url)
time.sleep(5)


def login():
    driver.get(login_url)
    time.sleep(5)
    login_email = driver.find_element_by_id("login-email")
    login_email.send_keys(USERNAME)
    time.sleep(5)
    login_password = driver.find_element_by_id("login-password")
    login_password.send_keys(PASSWORD)
    login_password.send_keys(Keys.ENTER)
    time.sleep(5)


# search for items to message
# create search list for items
watch_list = ("washer",
              "washing machine",
              "gaming chair",
              "Netball",
              "monitor",
              "desktop",
              "playstation",
              "tv",
              "television",
              "bike",
              "bicycle",
              "Samsung",
              "surfboard",
              "board game",
              "monopoly",
              "nintendo",
              "apple",
              "imac",
              "pram",
              "boat",
              )

excluded_words = ("broken",
                  "faulty",
                  "repair",
                  "parts",
                  "damage",
                  "for parts",
                  "not working"
                  )

page = 1
free_url = "https://www.gumtree.com.au/sydney/page-" + str(page) + "l3003642r20?price-type=free"

driver.get(free_url)
driver.set_page_load_timeout(5)

# prepare message template
message_template = "Hey you! Is this still available? Super keen. When do you need it gone by? Let's set a time :)"


# search if description has keywords
def selectAd():
    count = 1
    xPath = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[3]/main/section/div[2]/div/a["
                                         + str(count) + "]/div[2]/div/p")
    xPath.click()
    time.sleep(3)

    item_found = False
    ad_container = driver.find_element_by_xpath(f"//*[@class='vip-ad__container']")
    print("Searching through watch_list\n============================")
    for word in watch_list:
        try:
            search_keywords = ad_container.find_element_by_xpath(f".//*[contains(text(), \"{word}\")]")
            if search_keywords:
                print(f'Found Keyword \"{word}\" in \"{search_keywords.text}\"')
                item_found = True
        except exceptions.NoSuchElementException:
            print(f"Keyword \"{word}\" not found")

    print("\nSearching through excluded_words\n================================")
    for word in excluded_words:
        try:
            search_keywords = ad_container.find_element_by_xpath(f".//*[contains(text(), \"{word}\")]")
            if search_keywords:
                print(f'Found Keyword \"{word}\" in \"{search_keywords.text}\"')
                item_found = False
        except exceptions.NoSuchElementException:
            print(f"Keyword \"{word}\" not found")
    return item_found


    if search_keywords != watch_list or search_keywords == excluded_words:
        driver.back()
        count += 1
    else:
        message_box = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[3]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/form/div[1]/textarea")
        message_box.send_keys(Keys.CONTROL + "a")
        message_box.send_keys(message_template)
        time.sleep(randint(1, 3))
        send_message = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div/div[2]/button")
        send_message.click()
        driver.back()
        count += 1


send_email = selectAd()

# change search results to max

# run all functions parallel


# driver.quit()
