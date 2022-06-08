from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("Users/HP/Downloads/chromedriver")
browser.get(start_url)
time.sleep(10)

def scarp():
    headers=["Proper name", "Distance (ly)", "Mass (M☉)", "Radius (R☉)"]
    stars_data=[]

    for i in range(0,428):
        soup=BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={})
