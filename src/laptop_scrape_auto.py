from bs4 import BeautifulSoup
import requests
import json
import os.path

src_link = 'https://www.sastodeal.com/electronic/laptops.html'
pageNo = 1

pages = []
if( not (os.path.exists("files/laptop_scrape.json"))):
    # JSON file created
    with open("files/laptop_scrape.json", "w") as f:
        initial = {}
        json.dump(initial, f)
        f.close()

    # Default link
    link = src_link

    # # Done pages list created (to write)
    
    pages.append(link)

else:
    with open("files/laptop_scrape.json", "r") as f:
        data = f.read()
        wholePage = json.loads(data)
        for i in wholePage:
            pageNum = i
        # pageNo show current page initially and then increments
        pageNo = int(pageNum)
        # print(type(pageNo))
        link = wholePage[str(pageNo)]['nextpage']
        pageNo = pageNo + 1

# Main Scraping: for each page

url = requests.get(link)
print("Current Link: ", link)
html = BeautifulSoup(url.content, "html.parser")

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
    # print(laptop_list)     

# FInd next link in this page

try:
    nextlink = html.find(["a"], title='Next').attrs.get("href")
    pages.append(nextlink)

# Next link not exist
except AttributeError:
    nextlink = "-1"
    print("Erorrrr")

page_list = {
    'mypage': link, 
    'nextpage': nextlink,
    'laptops_details': laptop_list
}
# print(page_list)

with open("files/laptop_scrape.json", "r+") as f:
    file_data = f.read()
    red = json.loads(file_data)
    # print(red)
    
    red.update({ str(pageNo): page_list})
    f.seek(0)
    json.dump(red, f, indent = 4)



