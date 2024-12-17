from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import datetime
import requests

def hangang():
    url = "https://hangang.life/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('div', {"class": "fullscreen"})

    return {"unit": "\u00b0C", "number":results[0].find("span").string.split("|")[1].split("°")[0].strip(), "template": "big-number","image": "hangang"}

def clorox():
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

app = Flask(__name__)

@app.route('/')
def home():
    try:
        now = datetime.datetime.now() + datetime.timedelta(hours=9)
        crawls = [{"template": "clock","date": now.strftime("%y/%m/%d(%a)"), "time": now.strftime("%H:%M")}]

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