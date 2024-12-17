from flask import Flask, jsonify
# from fake_useragent import UserAgent
# import requests
# from bs4 import BeautifulSoup
import datetime

import hangang
import clorox

app = Flask(__name__)

@app.route('/')
def home():
    try:
        now = datetime.datetime.now() + datetime.timedelta(hours=9)
        crawls = [{"template": "clock","date": now.strftime("%y/%m/%d(%a)"), "time": now.strftime("%H:%M")}]

        crawls.append(hangang.crawl())
        crawls.append(clorox.crawl())

        return jsonify(crawls), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/about')
def about():
    return 'About'

if __name__ == "__main__":
    app.run()