from bs4 import BeautifulSoup
import requests
import json
import os

<<<<<<< HEAD
# Globals:

src_link = "https://www.sastodeal.com/electronic/laptops.html"
file_path = "files/laptop_scrape.json"


# Functions:

def getLinkFrom(json_file, mode):
    with open(json_file, mode) as f:
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
    page_no, link, json_dict = getLinkFrom(file_path, "r")
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
=======
src_link = "https://www.sastodeal.com/electronic/laptops.html"
json_file = "files/laptop_scrape.json"

def laptopScrape(file_path):
    # For pages except page 1:
    # load the json_dict,
    # find page no and
    # construct link.
    try:
        with open(file_path, "r") as f:
            json_dict = json.load(f)
            page_no = int(json_dict["last_page"]) + 1
            link = src_link + "?p=" + str(page_no)

    # If page 1: declare.
    except FileNotFoundError:
        page_no = 1
        link = src_link
        json_dict = {"laptops": [], "last_page": None}


    # Main Scraping: Done for each page.

    # Variable declaration:
    url = requests.get(link)
    print("Current Link: ", link)
    html = BeautifulSoup(url.content, "html.parser")

    # If last page: exit.
    if html.find("div", class_="message info empty"):
        print("Page non existent")
        quit()

    main_page = html.find(["ol"], class_="products list items product-items")
    laptops = main_page.findAll(["div"], class_="product-item-info")

    laptop_list = []

    # For each laptop, in each page:
    for laptop in laptops:
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
        laptop_list.append(laptop_info)

    #  Writing scraped info to JSON File:
    # save last_page no,
    # append new scraped laptops and
    # dump to file.
    with open(file_path, "w") as f:
        json_dict["last_page"] = page_no
        json_dict["laptops"].extend(laptop_list)
        json.dump(json_dict, f, indent=4)
        return laptop_list

laptopScrape(json_file)
>>>>>>> tests
