import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.sharesansar.com/newsdetail/investors-group-are-forewarning-that-the-brokers-license-suspension-would-result-in-them-protesting-on-the-streets-2022-11-07')
html = BeautifulSoup(url.content, "html.parser")

# TBD: extract only from the selected class    
def content():
    if html.find('div', class_ = 'col-md-12'):
        paras = html.findAll('p')
        content = ""
        for para in paras:
            content = content + para.get_text() 
        return content

# TBD: find images only in the class
def download_image():
    imgs = html.find_all("img")[2]
    imglink = imgs.attrs.get("src")
    # print(imglink)

    image = requests.get(imglink).content
    f = r"files" + imglink [imglink.rfind("/"):]
    
    with open(f, "wb") as file:
        file.write(image)

def links():
    pass

def title():
    title = html.title.get_text()
    return title

def savefile():
    toFile = ""
    toFile = title() + '\n\n\n' + content()

    f = open("files/sharesansar.txt", "w")
    f.write(toFile)
    f.close()

    print("text copied to sharesansar.txt")

# savefile()
download_image()