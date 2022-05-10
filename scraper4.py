from bs4 import BeautifulSoup
import requests
import re


search_item = input("What product do you search for? ")
url = f"https://www.newegg.ca/p/pl?d={search_item}&N=4131"
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')

page_text = doc.find(class_='list-tool-pagination-text').strong
pages = int(str(page_text).split('/')[-2].split('>')[-1][:1])

items_found = {}

for page in range(1, pages+1):
    url = f"https://www.newegg.ca/p/pl?d={search_item}&N=4131&page={page}"
    result = requests.get(url).text
    doc = BeautifulSoup(result, 'html.parser')

    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(search_item))

    for item in items:
        parent = item.parent
        if parent.name != 'a':
            continue
        link = parent['href']
        next_parent = parent.findParent(class_="item-container")
        price = int(next_parent.find(class_='price-current').strong.string.replace(',',''))
        items_found[item] = {
            'price': price,
            'link': link
        }

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])
for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("------------------------")



