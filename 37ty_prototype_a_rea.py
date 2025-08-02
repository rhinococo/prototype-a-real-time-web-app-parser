# 37ty_prototype_a_rea.py

import requests
from bs4 import BeautifulSoup
import time
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

def get_webpage_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def parse_webpage_data(soup):
    data = {}
    # parse specific data from the webpage
    title = soup.find('title').text
    paragraphs = [p.text for p in soup.find_all('p')]
    data['title'] = title
    data['paragraphs'] = paragraphs
    return data

@app.route('/parse', methods=['POST'])
def parse_webpage():
    url = request.form['url']
    soup = get_webpage_data(url)
    data = parse_webpage_data(soup)
    return jsonify(data)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)