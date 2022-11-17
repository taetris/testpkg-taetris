from bs4 import BeautifulSoup
import requests
import json
import os
# dict inside dict, append

pageDict = {'laptops': [],
            'lastPage': None}
src_link = 'https://www.sastodeal.com/electronic/laptops.html'
pageNo = 1
filePath = "files/laptop_scrape.json"

try:
    with open(filePath, "r") as f:
        data = f.read()
        pageDict = json.loads(data)
        pageNo = int(pageDict['lastPage'])
        pageNo = pageNo + 1
        link = src_link + "?p=" + str(pageNo)
except FileNotFoundError:
    link = src_link   

# Main Scraping: for each page

url = requests.get(link)
print("Current Link: ", link)
html = BeautifulSoup(url.content, "html.parser")

if html.find("div", class_ = "message info empty"):
        print("Page non existent")
        exit(1)
mainpage = html.find(["ol"], class_ = "products list items product-items")
laptops = mainpage.findAll(["div" ], class_ = 'product-item-info')

laptop_list = []

# FOr each laptop in each page

for laptop in laptops:
    laptop_name = laptop.find(["a"], class_ = "product-item-link").get_text()
    laptop_url = laptop.find(["a" ], class_ = 'product photo product-item-photo').attrs.get("href")
    price = laptop.find(['span'], class_ = 'price').get_text()
    img_url_all = laptop.find(['img']).attrs.get("src") 

    if "static.sastodeal.com" in img_url_all:
        img_url = img_url_all

    laptop_info = {'laptop_name': laptop_name,
                    'laptop_url': laptop_url,
                    'img_url': img_url,
                    'price': price,
                    
                    }

    # print(
    #     'laptop name:',laptop_name, '\n\n', 
    #     'laptop_url: ',laptop_url, '\n\n', 
    #     'price: ', price, '\n\n',
    #     'img_url: ', img_url, '\n\n'
    #     )
    laptop_list.append(laptop_info) 

with open(filePath, "w") as f:  
    pageDict['lastPage'] = pageNo
    pageDict['laptops'].extend(laptop_list)
    json.dump(pageDict, f, indent = 4)



