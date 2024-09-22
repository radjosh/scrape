from bs4 import BeautifulSoup
import selenium
import scrapy
import requests

TEST_URL = 'https://www.scrapingcourse.com/ecommerce/'

response = requests.get(TEST_URL)
print(response)