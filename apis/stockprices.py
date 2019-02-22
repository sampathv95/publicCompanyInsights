import numpy as np
import requests
import alphavantage
import datetime

def stockprice(ticker):
    url_gen='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&'+'symbol='+ticker+'&apikey= 55V43F1GP2CO3OW9'
    stockData=requests.get(url_gen).json()
    now = datetime.datetime.now()
    yesterday = datetime.datetime.now().strftime('%Y-%m-') + str(int(datetime.datetime.now().strftime('%d')) - 1)
    # print(stockData["Time Series (Daily)"][str(now)[:10]] == None)
    if str(now)[:10] in stockData["Time Series (Daily)"]:
        response = stockData["Time Series (Daily)"][str(now)[:10]]
        # print("now does not exist")
    else: 
        # print(yesterday)
        # print("date value ", response["Time Series (Daily)"][yesterday])
        response = stockData["Time Series (Daily)"][yesterday]
    return response