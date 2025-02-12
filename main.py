from flask import Flask, json

app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello Ace'
