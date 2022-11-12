import json
with open("files/laptop_scrape.json", "r") as f:
    data = f.read()
    laptops = json.loads(data)
    # print(laptops[-1]['price'])
    # for laptop in laptops:
    #     print("Name:     ", laptop['laptop_name'])
    #     print("Price:    ", laptop['price'], '\n')

