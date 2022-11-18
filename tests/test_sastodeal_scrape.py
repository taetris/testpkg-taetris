import pytest
import src.sastodeal_scrape as s 

def setUp():
    src_link = "https://www.sastodeal.com/electronic/laptops.html"
    file_path = "files/laptop_scrape.json"

def tearDown():
    pass

def test_getLinkFrom():
    print( getLinkFrom(file_path, "r") )

def test_searchLaptopInfoIn():
    pass

def test_initialize():
    # return page_no, link, json_dict
    pass

def test_getContentFrom():
    # return html
    pass

def test_writeScrapedInfoTo():
    pass

