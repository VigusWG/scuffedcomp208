from flask import Flask, json
import yfinance
import pandas

app = Flask(__name__)

@app.route('/')
def main():
    return 'random github'

@app.route('/api/stocks')
def getstocks():
    return {}

@app.route('/api/stockdata')
def stockd():
    thingy = yfinance.Ticker("MSFT")
    a: pandas.DataFrame = thingy.history(period="5y")
    print(a)
    x = {"labels": a.index.strftime('%d-%m-%Y').tolist(), "Opens": a.get('Open').tolist(), "Closes": a.get('Close').tolist()}
    return x

app.run()