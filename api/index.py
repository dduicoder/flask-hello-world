from flask import Flask, jsonify


import hangang
# import clorox

crawl_list = [hangang]

app = Flask(__name__)

@app.route('/')
def home():
    try:
        crawls = [{"dd":"dd"}]

        for crawl_module in crawl_list:
            crawls.append(crawl_module.crawl())

        return jsonify(crawls), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/about')
def about():
    return 'About'