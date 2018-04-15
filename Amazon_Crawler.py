# Amazon Product Review Crawler - Galaxy S7

import re
from selenium import webdriver
import csv
from bs4 import BeautifulSoup
from time import sleep

def reviews_info(div):
    review_text = div.find("div", "a-row review-data").span.text
    #review_author = div.find("a", "a-size-base a-link-normal author").text
    #review_stars = div.find("div", "a-row").a.text
    #on_review_date = div.find('span', 'a-size-base a-color-secondary review-date').text
    #review_date = [x.strip() for x in re.sub("on ", "", on_review_date).split(",")]

    return {
        "review_text": review_text,
        #"review_author": review_author,
        #"review_stars": review_stars,
        #"review_date": review_date
    }

base_url = "https://www.amazon.com/Samsung-Galaxy-S7-Smartphone-International/product-reviews/B01CJSF8IO/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=avp_only_reviews&pageNumber="
# You can easily get this URL by accessing the following route: Proudct > Customer reviews > See all verified purchase reviews.

driver = webdriver.PhantomJS()
reviews = []
NUM_PAGES = 53
# You have to change this number, since the number of review pages would be definitely different by products.
# On May 3, Galaxy S7 has 53 pages of reviews.

for page_num in range(1, NUM_PAGES + 1):
    print("souping page", page_num, ",", len(reviews), "data have been crawled.")
    url = base_url + str(page_num)
    print(url)
    driver.get(url)
    sleep(3)
    #driver.save_screenshot('screen.png')  # save a screenshot to disk
    data = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(data, 'lxml')
    for div in soup('div', 'a-section review'):
        reviews.append(reviews_info(div))


keys = reviews[0].keys()

driver.quit()

with open('amazon_GalaxyS7_review.txt', 'w', encoding="utf-8") as f: #store the data as a txt file.
    dict_writer = csv.DictWriter(f, delimiter=',', lineterminator='\n', fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(reviews)