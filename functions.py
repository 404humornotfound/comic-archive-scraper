import requests
from bs4 import BeautifulSoup as bs
from zipfile import ZipFile
import os

class Webtoon:
    def __init__(self, url:str):
        self.url = url
        if "WebToons" not in url:
            print("error: tool only designed to work on webtoons")
            exit()
        
        self.name = url[url.index("/WebToons/")+10:url.index("?")]
        os.makedirs(f"{self.name}")
        self.chapter_number = url[url.index("=")+1:url.index("-")]
        self.chapter_name = ""
        for i in 3-len(str(self.chapter_number)):
            self.chapter_name += "0"
        self.chapter_name += str(self.chapter_number)

        print(f"name:{self.name}")
        print(f"chapter number:{self.chapter_number}")
        

    def create_chapter_folder(self):
        os.makedirs(f"{self.name}/ch{self.chapter_name}")

    def write_image(self, html_tag):
        link = html_tag.get('href')
        link = link.replace("#", "comic")
        link = link.replace("?strip=", "/")
        response = requests.get(link)
        string = str(html_tag)
        img_name = string[string.index(">")+1:string.index("</a>")]
        print(img_name)
        if response.status_code == 200:
            with open(f"{img_name}.jpg", "wb") as f:
                f.write(response.content)
        else:
            print(f"image download error: {response.status_code}")
            print(f"link:{link}")
            exit()


    def zip_chapter(self):
        directory = f"{self.name}/ch{self.chapter_number}"

def start(url:str):
    # url = input("Copy + paste the url of the comic you want to scrape. Ex. https://webcomicarchive.com/#/WebToons/PinchPoint?strip=1-000.jpg")
    if "https://webcomicarchive.com/" not in url:
        print("url is invalid (doesn't match https://webcomicarchive.com/)")
    else:
        result = requests.get(url).text
        soup = bs(result, features="html.parser")
    name = url[32:url.index("?")]
    print(f"name:{name}")
    
def create_chaper(manga_name:str, chapter_number:int):
    os.makedirs(":")