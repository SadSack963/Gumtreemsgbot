def login():
    time.sleep(10)
    login_email = driver.find_element_by_id("login-email")
    search_bar.send_keys(USERNAME)
    login_password = driver.find_element_by_id("login-password")
    search_bar.send_keys(Keys.ENTER)
    driver.get_screenshot_as_file("screenshot.png")
    print(driver.title)
    time.sleep(10)

login()

def priceFilter():
    filter_min = driver.find_element_by_id("input-srp-range-filter-min")
    filter_min.send_keys("70")
    filter_max = driver.find_element_by_id("input-srp-range-filter-max")
    filter_max.send_keys("420")
    filter_max.send_keys(Keys.ENTER)

priceFilter()

def searchItems():
    time.sleep(5)
    search_bar = driver.find_element_by_id("search-query")
    search_bar.send_keys(random.choice(search_list))
    time.sleep(2)
    location_change = driver.find_element_by_id("search-area")
    location_change.send_keys(Keys.CONTROL + "a")
    location_change.send_keys(Keys.DELETE)
    time.sleep(2)
    location_change.send_keys("sydney")
    location_change.send_keys(Keys.ENTER)

searchItems()
time.sleep(3)

search_list = ("iphone",
              "playstation",
              "ps4",
              "ps5",
              "google",
              "apple",
              "nintendo",
              "imac",
              "macbook",
              "laptop",
              "Samsung"
               )

for items in xPath:
    href = xPath.get_attribute('href')
    print(href)
    items.send_keys(Keys.ENTER)
    time.sleep(3)
    if allResults != watch_list or allResults == excluded_words:
        exit = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/div/button")
        exit.click()
        count += 1
        time.sleep(3)
    else:
        print("Item fit watch list ")

def selectAd():
    all_ads = driver.find_element_by_class_name("user-ad-row-new-design__main-content")
    all_ads.click()
    time.sleep(3)
    go_back = driver.find_element_by_class_name("back-to-results")
    go_back.click()
    time.sleep(3)
    #self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    #select_ad = driver.find_element_by_class_name("user-ad-row-new-design__main-content")
    #select_ad.click()
    all_ads = driver.find_elements_by_class_name("user-ad-row-new-design__main-content")
    all_ads.click(random.choice(all_ads))
    time.sleep(3)

selectAd()

def bot():
    count = 1
    page = 1
    pageIncrement = 10
    maxRetrieve = 100

    url = "https://www.gumtree.com.au/s-coogee-sydney/page-" + str(page) + "l3003642r20?price-type=free"

    driver.get(url)
    driver.set_page_load_timeout(5)

    while True:
        try:
            if pageIncrement*page > maxRetrieve:
                break

            if count > pageIncrement:
                count = 1
                page += 1

            xPath = "//ul[@id='srchrslt-adtable']/li//h6[@class='rs-ad-title']/a"
            title = driver.find_element_by_xpath(xPath)
            title.click()

            print(title)

        except:
            print("failed.")


bot()
