from bs4 import BeautifulSoup
import selenium
import requests

TEST_URL = 'https://www.scrapingcourse.com/ecommerce/'

response = requests.get(TEST_URL)
# print(response)

soup = BeautifulSoup(response.text, "html.parser")

product_names = soup.find_all("h2")

for product_name in product_names:
    print(product_name.text)

