import json

f = open("files/laptop_scrape.json", "r")
data = f.read()
laptops = json.loads(data)

for laptop in laptops:
    print("Name:     ", laptop['laptop_name'])
    print("Price:    ", laptop['price'], '\n')

