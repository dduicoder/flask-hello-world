import requests
from bs4 import BeautifulSoup

def crawl():
    url = "https://hangang.life/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('div', {"class": "fullscreen"})

    return {"unit": "\u00b0C", "number":results[0].find("span").string.split("|")[1].split("°")[0], "template": "big-number",}

if __name__ == "__main__":
    print(crawl())
