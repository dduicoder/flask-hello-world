import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def crawl():
    try:
        url = "https://yuhanrox.co.kr/Shop/16831"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36",
            "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
        }
        print(headers)

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        results = soup.find(id="sales_price")

        price = results.get_text()
        # print(results.get_text())
        return {
            "template": "big-number",
            "number": str(int(price) // 20),
            "unit": "원/100mL",
            "image": "clorox"
        }
    except:
        return {
            "template": "big-number",
            "number": "210",
            "unit": "원/100mL",
            "image": "clorox"
        }

if __name__ == "__main__":
    print(crawl())
