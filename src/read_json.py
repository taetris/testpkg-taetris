import json
from bs4 import BeautifulSoup
import requests

link = "https://www.sastodeal.com/electronic/laptops.html?p=3" 
url = requests.get(link)
html = BeautifulSoup(url.content, "html.parser")
# print(html)

if html.find("div", class_ = "message info empty"):
        print("wffeg")
# with open("files/laptop_scrape.json", "r") as f:
#     data = f.read()
#     laptops = json.loads(data)
#     # print(laptops[-1]['price'])
#     # for laptop in laptops:
#     #     print("Name:     ", laptop['laptop_name'])
#     #     print("Price:    ", laptop['price'], '\n')


        # pageNo = link[-1]
        # print(pageNo)
