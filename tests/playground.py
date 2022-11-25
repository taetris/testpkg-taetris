import pytest
import os
import src.sastodeal_scrape as s
import random

# code to run: pyhton3 -m tests.playground

def setup_functio():
    print("---------SetUp-------------")
    try:
        os.remove(r"files/laptop_scrape.json")
    except FileNotFoundError:
        pass



def input_file():
    return "files/laptop_scrape.json"


def first_laptop_name():
    first_laptop_name = [
        '\nlnspirion 15 GAMING SERIES - G5- i7-11800H-16GB(8x2)-512GB -15.6" 120Hz 250nits-\nRTX 3050Ti- 4GB-WS11 ',
        '\nDell G5 15 SE Gaming Laptop Ryzen 7 4800H / AMD RX 5600M 6144MB / 8GB RAM / 512GB SSD / 15.6" FHD 144Hz Display ',
        "\nDell G5-15 5511 | i7-11800H | 8GB | 512SSD | NVIDIA RTX 3050-4GB GDDR6 | FHD | Office 2019 ",
    ]
    return first_laptop_name


def laptopScrape_firstLaptop():
    setup_functio()
    input_fil = input_file()
    first_laptop_nam = first_laptop_name()
    for i in range(6):
        print( s.laptopScrape(input_fil)[1]) if 

laptopScrape_firstLaptop()