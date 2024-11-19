from flask import Flask, render_template
from data import fetch_finance_data

app = Flask(__name__)


@app.route("/")
def home():
    symbol = "AAPL"
    api_key = "F3DK9HXI8NGB85K1"
    dates, prices = fetch_finance_data(symbol, api_key)
    return render_template("index.html", symbol=symbol, dates=dates, prices=prices)


if __name__ == "__main__":
    app.run(debug=True)