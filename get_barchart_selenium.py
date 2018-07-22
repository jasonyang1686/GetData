# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:12:32 2018

@author: Shiming Yang
"""
import time
import datetime
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

def request_VIX_barchart(month, year):
    # https://cfe.cboe.com/trade-cfe/quote-vendor-symbols/vx-cboe-volatility-index-vix-futures
    # names are coded as FGHJKMNQUVXZ
    mCode = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z']
    url = 'https://www.barchart.com/futures/quotes/VI' + mCode[month - 1] + str(year)
    profile = webdriver.FirefoxProfile()
    options = Options()
    #options.set_preference("permissions.default.image",
    #                       2)
    options.set_headless(headless=True)
    profile.set_preference("permissions.default.image",
                           2)  # 1 allow all image, 2. disable all images, 3, disable 3rd site images
    driver = webdriver.Firefox(firefox_options=options,
                               executable_path="/Volumes/Macintosh HD/Study/quantopian/GetData/geckodriver",
                               firefox_profile=profile)
    #driver = webdriver.Chrome(chrome_options=options,
    #                           executable_path="/Volumes/Macintosh HD/Study/quantopian/GetData/chromedriver",
    #                           #chrome_profile=profile
    #                          )
    driver.get(url)

    last_change = driver.find_element_by_xpath('//*[@id="main-content-column"]/div/div[1]/div[2]/span[1]')
    last_change_value = last_change.text
    #    last_bid_price = driver.find_element_by_xpath('//*[@id="main-content-column"]/div/div[1]/div[3]/div/span[1]').text
    #    last_bid_size = driver.find_element_by_xpath('//*[@id="main-content-column"]/div/div[1]/div[3]/div/span[1]/span').text
    #    last_ask_price = driver.find_element_by_xpath('//*[@id="main-content-column"]/div/div[1]/div[3]/div/span[2]').text
    #    last_ask_size = driver.find_element_by_xpath('//*[@id="main-content-column"]/div/div[1]/div[3]/div/span[2]/span').text
    #
    driver.close()
    return last_change_value  # , last_bid_price,last_bid_size,last_ask_price,last_ask_size


if __name__ == "__main__":
    mCode = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z']
    current_year = datetime.now().strftime('%Y')
    current_month = datetime.now().month
    while True:
        last_price_current = request_VIX_barchart(current_month+1, current_year)
        last_price_next = request_VIX_barchart(current_month+2, current_year)
        print('VI' + mCode[current_month] + str(current_year) + ' current month''s last price is ' + last_price_current)
        print('VI' + mCode[current_month+1] + str(current_year) + ' next month''s last price is ' + last_price_next)
        time.sleep(20)
