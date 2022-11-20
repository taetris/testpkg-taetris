from bs4 import BeautifulSoup
import requests
import json
import os

# Globals:

src_link = "https://www.sastodeal.com/electronic/laptops.html"
file_path = "files/laptop_scrape.json"


# Functions:

def getLinkFrom(json_file):
    with open(json_file, "r") as f:
        json_dict = json.load(f)
        page_no = int(json_dict["last_page"]) + 1
        link = src_link + "?p=" + str(page_no)
    return page_no, link, json_dict

def searchLaptopInfoIn(laptop):
    laptop_name = laptop.find(["a"], class_="product-item-link").get_text()
    laptop_url = laptop.find(
        ["a"], class_="product photo product-item-photo"
    ).attrs.get("href")
    price = laptop.find(["span"], class_="price").get_text()
    img_url_all = laptop.find(["img"]).attrs.get("src")

    if "static.sastodeal.com" in img_url_all:
        img_url = img_url_all

    laptop_info = {
        "laptop_name": laptop_name,
        "laptop_url": laptop_url,
        "img_url": img_url,
        "price": price,
    }

    return laptop_info


def initialize():
    page_no = 1
    link = src_link
    json_dict = {"laptops": [], "last_page": None}
    return page_no, link, json_dict


def getContentFrom(link):
    url = requests.get(link)
    print("Current Link: ", link)
    html = BeautifulSoup(url.content, "html.parser")
    return html


def writeScrapedInfoTo(json_file, mode, json_dict):
    with open(json_file, mode) as f:
        json_dict["last_page"] = page_no
        json_dict["laptops"].extend(laptop_list)
        json.dump(json_dict, f, indent=4)
    return None


###         Main Code Starts Here           ###

# File Read:
try:
    page_no, link, json_dict = getLinkFrom(file_path)
except FileNotFoundError:
    page_no, link, json_dict = initialize()

# Scraping Each page

content = getContentFrom(link)

isLastPage = content.find("div", class_="message info empty")

if isLastPage:
    print("End of page chain")
    exit(1)

main_page = content.find(["ol"], class_="products list items product-items")
laptops = main_page.findAll(["div"], class_="product-item-info")

laptop_list = []

# Scrape each laptop, on each page:
for laptop in laptops:
    laptop_info = searchLaptopInfoIn(laptop)
    laptop_list.append(laptop_info)

# Write Out:

writeScrapedInfoTo(file_path, "w", json_dict)
