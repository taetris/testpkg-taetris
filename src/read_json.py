import json
from bs4 import BeautifulSoup
import requests

with open("files/laptop_scrape.json", "r+") as f:
        data = f.read()
        wholePage = json.loads(data)
        print(wholePage)
        wholePage['laptops_details'].append('blahahahhahahha')
        print(wholePage)
        f.seek(0)
        json.dump(wholePage,f, indent=4)



# with open("files/laptop_scrape.json", "r") as f:
#     data = f.read()
#     laptops = json.loads(data)
#     # print(laptops[-1]['price'])
#     # for laptop in laptops:
#     #     print("Name:     ", laptop['laptop_name'])
#     #     print("Price:    ", laptop['price'], '\n')


        # pageNo = link[-1]
        # print(pageNo)
