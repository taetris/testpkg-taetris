import pytest
import os
import src.sastodeal_scrape as s

@pytest.fixture
def input_file():
    return "files/laptop_scrape.json"

def test_laptopScrape_firstLaptop(input_file):
    os.remove(r'files/laptop_scrape.json')
    laptop1 = s.laptopScrape(input_file)[0]["laptop_name"] 
    laptop2 = s.laptopScrape(input_file)[0]["laptop_name"] 
    laptop3 = s.laptopScrape(input_file)[0]["laptop_name"] 

    assert laptop1 == "\nlnspirion 15 GAMING SERIES - G5- i7-11800H-16GB(8x2)-512GB -15.6\" 120Hz 250nits-\nRTX 3050Ti- 4GB-WS11 " and laptop2 ==  '\nDell G5 15 SE Gaming Laptop Ryzen 7 4800H / AMD RX 5600M 6144MB / 8GB RAM / 512GB SSD / 15.6" FHD 144Hz Display ' and laptop3 ==    "\nDell G5-15 5511 | i7-11800H | 8GB | 512SSD | NVIDIA RTX 3050-4GB GDDR6 | FHD | Office 2019 "

# def test_laptopScrape_pageSize():
#     os.remove(r'files/laptop_scrape.json')
#     pageSize1 = len(s.laptopScrape(input_file))
#     assert pageSize1 == 36

# tlaptopScrape()



# @pytest.mark.parametrize(
#     "first_laptop_name",
#     [    ("\nlnspirion 15 GAMING SERIES - G5- i7-11800H-16GB(8x2)-512GB -15.6\" 120Hz 250nits-\nRTX 3050Ti- 4GB-WS11 "),
#         (
#             '\nDell G5 15 SE Gaming Laptop Ryzen 7 4800H / AMD RX 5600M 6144MB / 8GB RAM / 512GB SSD / 15.6" FHD 144Hz Display '
#         ),
#         (
#             "\nDell G5-15 5511 | i7-11800H | 8GB | 512SSD | NVIDIA RTX 3050-4GB GDDR6 | FHD | Office 2019 "
#         ),
#     ],
# )
# def test_laptopScrape(input_file, first_laptop_name):
#     assert s.laptopScrape(input_file)[0]["laptop_name"] == first_laptop_name 
