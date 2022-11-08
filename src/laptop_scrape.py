from bs4 import BeautifulSoup
import requests
import json


# f = open("files/laptop_scrape.json", "w")
url = requests.get('https://www.sastodeal.com/electronic/laptops.html')
html = BeautifulSoup(url.content, "html.parser")

mainpage = html.find(["ol"], class_ = "products list items product-items")


laptops = mainpage.findAll(["div" ], class_ = 'product-item-info')

for laptop in laptops:
    laptop_name = laptop.find(["a"], class_ = "product-item-link").get_text()
    laptop_url = laptop.find(["a" ], class_ = 'product photo product-item-photo').attrs.get("href")
    price = laptop.find(['span'], class_ = 'price').get_text()
    
    print('laptop name:',laptop_name, '\n\n', 
    'laptop_url: ',laptop_url, '\n\n', 'price: ', price, '\n\n')
    img_url = laptop.find(['img']).attrs.get("src")
    if "static.sastodeal.com" in img_url:
        print('img_url: ', img_url, '\n\n')



# f.write(toFile)
# f.close()

