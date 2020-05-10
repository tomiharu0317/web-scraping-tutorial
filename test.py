import requests
from bs4 import BeautifulSoup
import re

url = "https://news.yahoo.co.jp"
response = requests.get(url)
some_text = response.text[:500]
print(some_text)

soup = BeautifulSoup(response.text, "html.parser")

elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
print(elems,'\n')

for elem in elems:
    print(elem.contents[0])
    print(elem.attrs['href'])
