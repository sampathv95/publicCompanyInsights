from flask import Flask, render_template, request
import os
import json
import  apis.stockprices 
from apis.stockprices import stockprice
from apis.news import news
import apis.financialdata
from apis.financialdata import financialNumbers
import apis.earningcalls
from apis.earningcalls import earningCallData
import apis.Model
from apis.Model import sentimentAnalyzer
app = Flask(__name__, static_folder="static")


from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__)
@app.route('/')
def root():
    return render_template('index.html')

@app.route('/api/stock', methods =["POST"])
def sendData():
    print("got the post request", request.data)
    data = json.loads(request.data)
    print(data.get('name'))
    company = data.get('name')
    response = dict()
    try:
        # #insight 1- stockprice
        response.update({'stockPrice':stockprice(company)})
        #insight-1 news
        #sentiment analysis of news
        newsValues=news(company)
        
        #sentiment analysis of news
        newsSentiment=sentimentAnalyzer(company)
        for i in range(len(newsValues['news'])):
            newsValues['news'][i]['sentiment']= int(newsSentiment[i])
        print(type(newsValues))
        response.update({'news':newsValues})
        # #insight3- financial numbers
        response.update({'finiancialNumbers':financialNumbers(company)})
        response.update({'earningCalls':earningCallData(company)})
    except:
        # print("exception")
        response =dict()
        response.update({'error':'There has been an error in retreving the data, Please try again later'})
    # print(response)
    return (json.dumps(response))
