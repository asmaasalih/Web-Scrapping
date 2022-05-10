from bs4 import BeautifulSoup
import requests
import re

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')

tbody = doc.tbody
trs = tbody.contents

prices = {}

for tr in trs:
    name, price = tr.contents[2:4]
    fixed_name = name.text
    fixed_price = price.text
    prices[fixed_name] = fixed_price
print(prices)
