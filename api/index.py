from flask import Flask, jsonify


import requests
from bs4 import BeautifulSoup

def hangang():
    url = "https://hangang.life/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('div', {"class": "fullscreen"})

    return {"name": "hangang", "value":results[0].find("span").string.split("|")[1].strip(), "template": "show",}

# import hangang
# import clorox

# crawl_list = [hangang]

app = Flask(__name__)

@app.route('/')
def home():
    try:
        crawls = [{"dd":"dd"}]

        crawls.append(hangang())

        return jsonify(crawls), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/about')
def about():
    return 'About'