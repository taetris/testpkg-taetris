import pytest
import src.sastodeal_scrape as s 

def test_getLinkFrom():
    assert s.getLinkFrom("files/laptop_scrape.json")[1] in ['https://www.sastodeal.com/electronic/laptops.html',
                                                            'https://www.sastodeal.com/electronic/laptops.html?p=2',
                                                            'https://www.sastodeal.com/electronic/laptops.html?p=3',
                                                            'https://www.sastodeal.com/electronic/laptops.html?p=4'
                                                            ]

def test_searchLaptopInfoIn():
    laptops = main_page.findAll(["div"], class_="product-item-info")

    assert s.searchLaptopInfoIn()

# def test_initialize():
#     # return page_no, link, json_dict
#     pass

# def test_getContentFrom():
#     # return html
#     pass

# def test_writeScrapedInfoTo():
#     pass

