import pytest
import os
import src.sastodeal_scrape as s
import random


def setup_function():
    print("---------SetUp-------------")
    try:
        os.remove(r"files/laptop_scrape.json")
    except FileNotFoundError:
        pass


@pytest.fixture
def input_file():
    return "files/laptop_scrape.json"


@pytest.fixture
def first_laptop_name():
    first_laptop_name = [
        '\nlnspirion 15 GAMING SERIES - G5- i7-11800H-16GB(8x2)-512GB -15.6" 120Hz 250nits-\nRTX 3050Ti- 4GB-WS11 ',
        '\nDell G5 15 SE Gaming Laptop Ryzen 7 4800H / AMD RX 5600M 6144MB / 8GB RAM / 512GB SSD / 15.6" FHD 144Hz Display ',
        "\nDell G5-15 5511 | i7-11800H | 8GB | 512SSD | NVIDIA RTX 3050-4GB GDDR6 | FHD | Office 2019 ",
    ]
    return first_laptop_name


def test_laptopScrape_firstLaptop(input_file, first_laptop_name):

    firstLaptop = []
    for i in range(3):
        assert s.laptopScrape(input_file)[0]["laptop_name"] in first_laptop_name


def test_laptopScrape_pageSize(input_file):

    for i in range(random.randint(0, 9)):
        assert len(s.laptopScrape(input_file)) <= 36


def test_laptopScrape_totalSize(input_file):
    totalSize = 0

    for i in range(random.randint(0, 9)):
        totalSize = totalSize + len(s.laptopScrape(input_file))
    assert totalSize <= 79


def test_laptopScrape_returnedFields(input_file):

    for i in range(random.randint(1, 3)):
        fields = list(s.laptopScrape(input_file)[random.randint(0, 6)].keys())
        assert fields in [["laptop_name", "laptop_url", "img_url", "price"], []]


def test_laptopScrape_ensureMultipleRun(input_file):

    laptopSet = set()
    for i in range(3):
        laptop_no = random.randint(0, 6)
        laptopSet.add(s.laptopScrape(input_file)[laptop_no]["laptop_name"])
    assert len(laptopSet) == len(set(laptopSet))
