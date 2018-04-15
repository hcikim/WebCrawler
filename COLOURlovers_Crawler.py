# Python3

import re
from selenium import webdriver
import csv
from bs4 import BeautifulSoup
#from time import sleep

def reviews_info(div):
    color_infos = []
    color_names = div.find("h3", "left mr-10").a.text
    #color_meta = div.find_all("div", "meta").div.h4.text
    color_hex = div.find("div", "col-70 big-number-label").h4.text
    color_rgb = div.find("div", "col-80 big-number-label").h4.text
    #for i in range(4):
    #    color_info = div.find("div", "right-col big-number-label").h4.text[0]
    #    color_infos.append(color_info)

    return {
        "color_name": color_names,
        "color_hex": color_hex,
        "color_rgb": color_rgb,
    #    "comment | favoirites | views | loves": color_infos
    }

base_url = "http://www.colourlovers.com/colors/most-favorites/all-time/meta?page="

driver = webdriver.PhantomJS()
reviews = []
NUM_PAGES = 5 # change this number as you wish

# 655570
# 53232 Top fav to Bottom
# Crawl the data until it has no favorite. (Manually checked the page on 30 June 2017)

for page_num in range(1, NUM_PAGES + 1):
    print("souping page", page_num, ",", len(reviews), "data have been crawled.")
    url = base_url + str(page_num)
    print(url)
    driver.get(url)
    #sleep(3)
    #driver.save_screenshot('screen.png')  # Save a screenshot to disk
    data = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(data, 'lxml')
    for div in soup('div', 'detail-row'):
        reviews.append(reviews_info(div))
    #sleep(5)


keys = reviews[0].keys()

driver.quit()

with open('colourlover.csv', 'w', encoding="utf-8") as f:
    dict_writer = csv.DictWriter(f, delimiter=',', lineterminator='\n', fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(reviews)