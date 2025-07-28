import requests
from bs4 import BeautifulSoup as bs
url = "https://webcomicarchive.com/#/WebToons/PinchPoint?strip=1-000.jpg"
result = requests.get(url).text
soup = bs(result, features="html.parser")

tags = soup.find_all("list-group list-group-flush")
print(tags)
# https://webcomicarchive.com/comic/WebToons/PinchPoint/1-001.jpg

# class = list-group list-group-flush  ... id = sidebarStrips
