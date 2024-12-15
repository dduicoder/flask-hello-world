import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def crawl():
    url = "https://www.coupang.com/np/search?component=&q=%EC%9C%A0%ED%95%9C%EB%9D%BD%EC%8A%A4&channel=user"

    headers = {
        "User-Agent": UserAgent().random,
        "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('em')
    print(results)
    return {"name": "clorox", "value": "350 KRW/100mL", "template": "show",}

if __name__ == "__main__":
    print(crawl())
