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

# prepare message template
message_template = "Hey you! Is this still available? Super keen. When do you need it gone by? Let's set a time :)"

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


def login():
    # url = "https://www.gumtree.com.au/"
    # driver.get(url)
    # time.sleep(5)

    login_url = "https://www.gumtree.com.au/t-login-form.html"
    driver.get(login_url)
    time.sleep(5)
    login_email = driver.find_element_by_id("login-email")
    login_email.send_keys(USERNAME)
    time.sleep(5)
    login_password = driver.find_element_by_id("login-password")
    login_password.send_keys(PASSWORD)
    login_password.send_keys(Keys.ENTER)
    time.sleep(5)


def search_ads():
    results = []
    ads_section = driver.find_element_by_xpath('//*[@id="react-root"]/div/div[3]/div/div[3]/main/section')
    user_ad_list = ads_section.find_elements_by_tag_name('a')

    for user_ad in user_ad_list:
        item_found = False
        ad_href = user_ad.get_attribute('href')
        ad_title = user_ad.find_element_by_class_name('user-ad-row-new-design__title-span').text
        ad_description = user_ad.find_element_by_class_name('user-ad-row-new-design__description-text').text

        print("Searching through watch_list\n============================")
        for word in watch_list:
            if word.lower() in ad_title.lower() or word.lower() in ad_description.lower():
                print(f'Found Watch Word: \"{word}\"')
                item_found = True
                break

        print("\nSearching through excluded_words\n================================")
        for word in excluded_words:
            if word.lower() in ad_title.lower() or word.lower() in ad_description.lower():
                print(f'Found Excluded Word: \"{word}\"')
                item_found = False
                break

        if item_found:
            results.append(
                {
                    'href': ad_href,
                    'title': ad_title,
                    'description': ad_description,
                }
            )

    return results


chrome_driver_path = "E:/Python/WebDriver/chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

driver.set_page_load_timeout(15)

url = "https://www.gumtree.com.au/s-electronics-computer/sydney/smart+tv/k0c20045l3003435?price=__20.00"
driver.get(url)

search_results = search_ads()
print(search_results)
