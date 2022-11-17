from bs4 import BeautifulSoup
import requests
import json
import os
# dict inside dict, append

pageDict = {'laptops': [],
            'lastPage': None}
src_link = 'https://www.sastodeal.com/electronic/laptops.html'
pageNo = 1

if( not (os.path.exists("files/laptop_scrape.json"))):
    # Default link
    link = src_link

else:
    with open("files/laptop_scrape.json", "r") as f:
        data = f.read()
        pageDict = json.loads(data)
        pageNum = pageDict['lastPage']
        # pageNo show current page initially and then increments
        pageNo = int(pageNum)
        # print(type(pageNo))
        pageNo = pageNo + 1
        link = src_link + "?p=" + str(pageNo)
        # print(wholePage) 



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

with open("files/laptop_scrape.json", "w") as f:
    
    pageDict['lastPage'] = pageNo
    pageDict['laptops'].extend(laptop_list)
    f.seek(0)
    json.dump(pageDict, f, indent = 4)



