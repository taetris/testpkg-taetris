import requests
from bs4 import BeautifulSoup

header = {"User Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"}
url = requests.get('https://www.daraz.com.np/products/nikon-d3500-af-p-dx-18-55mm-f35-56g-vr-i118702256-s1032525442.html?spm=a2a0e.searchlistcategory.list.2.6e604414mvpT7b&search=1')

html = BeautifulSoup(url.content, "html.parser")
# print(html)                                  
images = html.find("img")
print(images)


