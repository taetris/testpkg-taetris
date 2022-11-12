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
        link = wholePage.keys()[-1]['nextpage']
        print(link)
        pageNo = link[-1]
        print(pageNo)

# Main Scraping: for each page
url = requests.get(link)
html = BeautifulSoup(url.content, "html.parser")
# print(pagesdone)
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

# FInd next link in this page
nextlink = html.find("a", title='Next').attrs.get("href")
# print(nextlink)
try:
    pages.append(nextlink)
    print(pages)
# Next link not exist
except AttributeError:
    nextlink = "-1"

page_list = {
    'mypage': link, 
    'nextpage': nextlink,
    'laptops_details': laptop_list
}


with open("files/laptop_scrape.json", "r+") as f:
    file_data = f.read()
    # print(file_data)
    red = json.loads(file_data)
    # print(red)
    title = str(pageNo)
    red.update({ title: page_list})
    # print(red)
    # # # Sets file's current position at offset.
    f.seek(0)
    json.dump(red, f, indent = 4)



