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

webtoon = Webtoon(url)


with open("w.html", "r", encoding="utf8") as f:
    soup = bs(f, "html.parser")

tags = soup.find_all("a", class_ = "list-group-item block", href=True)
tags.insert(0, soup.find_all("a", class_="list-group-item block border-top-0", href=True))

for i in tags[:10]:
    if not os.path.isdir(f"ch{webtoon.chapter_name}"):
        webtoon.create_chapter_folder()

