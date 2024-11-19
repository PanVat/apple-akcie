import requests


def fetch_finance_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        time_series = data.get('Time Series (Daily)', {})
        dates = []
        prices = []
        for date, values in time_series.items():
            dates.append(date)
            prices.append(float(values['4. close']))
        return dates, prices
    else:
        print("Error during data retrieval: ", response.status_code)
        return [], []
