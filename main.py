from flask import Flask, json, request, render_template
import yfinance
import csv

app = Flask(__name__)
stocks = {}
with open('stock_info.csv') as r:
    reader = csv.reader(r)
    for row in reader:
        if row[2] == "NASDAQ": 
            stocks[row[1]] = row[0]

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/api/stocks')
def getstocks():
    search = request.args.get('s')
    if not search:
        return {"error": "enter something"}
    return {"data": [[i, stocks[i]] for i in stocks.keys() if i.lower().startswith(search.lower())][:10]}

@app.route('/api/stockdata')
def stockd():
    stock = request.args.get('s')
    if not stock:
        return {"error": "enter something"}
    thingy = yfinance.Ticker(stock)
    # if not thingy.fast_info():   ## fuck it theyre big boys we dont need to error handle this for now
    #     return {"error": "Unknown stock"}
    
    a = thingy.history(period="5y")
    x = {"labels": a.index.strftime('%d-%m-%Y').tolist(), "Opens": a.get('Open').tolist(), "Closes": a.get('Close').tolist()}
    return x

app.run()