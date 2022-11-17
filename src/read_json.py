import json
from bs4 import BeautifulSoup
import requests

with open("files/laptop_scrape.json", "r") as f:
        data = f.read()
        wholePage = json.loads(data)
        for i in wholePage:
            
            print(i['current_page'])
# with open("files/laptop_scrape.json", "r") as f:
#     data = f.read()
#     laptops = json.loads(data)
#     # print(laptops[-1]['price'])
#     # for laptop in laptops:
#     #     print("Name:     ", laptop['laptop_name'])
#     #     print("Price:    ", laptop['price'], '\n')


        # pageNo = link[-1]
        # print(pageNo)
