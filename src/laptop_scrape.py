from bs4 import BeautifulSoup
import requests
import json

with open("files/laptop_scrape.json", "w") as f:
    f.close()

src_link = 'https://www.sastodeal.com/electronic/laptops.html'
link = src_link
pages = []
pages.append(link)
for page in pages:  
    url = requests.get(link)
    html = BeautifulSoup(url.content, "html.parser")
    print(pages)
    mainpage = html.find(["ol"], class_ = "products list items product-items")
    laptops = mainpage.findAll(["div" ], class_ = 'product-item-info')

    laptop_list = []

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
                        'price': price
                        }

        laptop_list.append(laptop_info)         

        # print('laptop name:',laptop_name, '\n\n', 
        # 'laptop_url: ',laptop_url, '\n\n', 'price: ', price, '\n\n')
        # if "static.sastodeal.com" in img_url:
        #     print('img_url: ', img_url, '\n\n')


    with open("files/laptop_scrape.json", "a") as f:
        json.dump(laptop_list, f, indent = 4)
    link = html.find("a", title='Next').attrs.get("href")

    try:
        pages.append(link)
    except AttributeError:
        print("loop ended")
        break
    
