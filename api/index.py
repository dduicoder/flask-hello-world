from flask import Flask, jsonify
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

def hangang():
    url = "https://hangang.life/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('div', {"class": "fullscreen"})

    return {"unit": "°C", "number":results[0].find("span").string.split("|")[1].split("°")[0], "template": "big-number","image":"hangang",}


def clorox():
    # url = "https://www.coupang.com/np/search?component=&q=%EC%9C%A0%ED%95%9C%EB%9D%BD%EC%8A%A4&channel=user"

    # headers = {
    #     "User-Agent": UserAgent().random,
    #     "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
    # }

    # response = requests.get(url, headers=headers)

    # soup = BeautifulSoup(response.text, 'html.parser')

    # results = soup.find_all('em')
    # print(results)
    return {
		"template": "big-number",
		"number": "1300",
		"unit": "원/100mL",
		"image": "clorox"
	}

app = Flask(__name__)

@app.route('/')
def home():
    try:
        crawls = [{"template": "clock"}]

        crawls.append(hangang())
        crawls.append(clorox())

        return jsonify(crawls), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/about')
def about():
    return 'About'

if __name__ == "__main__":
    app.run()