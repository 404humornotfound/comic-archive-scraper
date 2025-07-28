import requests
from bs4 import BeautifulSoup as bs
from zipfile import ZipFile
import os
from os.path import basename
from functions import *
import time
url = "https://webcomicarchive.com/#/WebToons/PinchPoint?strip=1-000.jpg"
# result = requests.get(url).text
# soup = bs(result, features="html.parser")
"""
pure jpg: 
https://webcomicarchive.com/comic/WebToons/PinchPoint/1-000.jpg

big html:
https://webcomicarchive.com/#/WebToons/PinchPoint?strip=1-000.jpg


plan: change # to comic and change ?strip= to /


"""
# start("https://webcomicarchive.com/#/WebToons/PinchPoint?strip=1-000.jpg")


with open("w.html", "r", encoding="utf8") as f:
    soup = bs(f, "html.parser")

tags = soup.find_all("a", class_ = "list-group-item block", href=True)
tags.insert(0, soup.find_all("a", class_="list-group-item block border-top-0", href=True))


i = tags[0][0]
time.sleep(5)
lnk = i.get('href')
lnk = lnk.replace("#", "comic")
lnk = lnk.replace("?strip=", "/")

response = requests.get(lnk)
if response.status_code == 200:
    with open("a.jpg", "wb") as f:
        f.write(response.content)
else:
    print(f"error: {response.status_code}")

