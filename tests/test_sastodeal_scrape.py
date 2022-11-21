import pytest
import src.sastodeal_scrape as s


@pytest.fixture
def input_file():
    return "files/laptop_scrape.json"


@pytest.mark.parametrize(
    "first_laptop_name",
    [
        (
            '\nDell G5 15 SE Gaming Laptop Ryzen 7 4800H / AMD RX 5600M 6144MB / 8GB RAM / 512GB SSD / 15.6" FHD 144Hz Display '
        ),
        (
            "\nDell G5-15 5511 | i7-11800H | 8GB | 512SSD | NVIDIA RTX 3050-4GB GDDR6 | FHD | Office 2019 "
        ),
    ],
)
def test_laptopScrape(input_file, first_laptop_name):
    assert s.laptopScrape(input_file)[0]["laptop_name"] == first_laptop_name
