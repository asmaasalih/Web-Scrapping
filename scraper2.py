from bs4 import BeautifulSoup
import re


with open('index.html', 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')
tags = doc.find_all(text=re.compile('\$.*'))
for tag in tags:
    print(tag.strip())

input_tags = doc.find_all('input', type='text')
for tag in input_tags:
    tag['placeholder'] = 'I changed it'

with open('changed.html','w') as file:
    file.write(str(doc))

