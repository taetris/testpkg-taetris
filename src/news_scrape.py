import requests
from bs4 import BeautifulSoup

header = {"User Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"}
url = requests.get('https://www.sharesansar.com/newsdetail/investors-group-are-forewarning-that-the-brokers-license-suspension-would-result-in-them-protesting-on-the-streets-2022-11-07')
html = BeautifulSoup(url.content, "html.parser")
         
def content():
    if html.find('div', class_ = 'col-md-12'):
        paras = html.findAll('p')
        content = ""
        for para in paras:
            content = content + para.get_text() + '\n\n'
        return content

def image():
    pass

def links():
    pass

def title():
    title = html.title.get_text()
    return title

print(title(),"\n\n\n", content())


