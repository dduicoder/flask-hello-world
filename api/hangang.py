import requests
from bs4 import BeautifulSoup

def crawl():
    url = "https://hangang.life/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('div', {"class": "fullscreen"})

    return {"name": "hangang", "value":results[0].find("span").string.split("|")[1].strip(), "template": "show",}

if __name__ == "__main__":
    print(crawl())
