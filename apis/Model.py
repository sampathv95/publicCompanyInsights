# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 00:41:56 2019

@author: sam
"""

import pickle
import apis.news
from apis.news import news
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import os

dirname = os.path.dirname(__file__)
Pickled_model = os.path.join(dirname, 'Pickled_model.sav') 
loaded_model = pickle.load(open(Pickled_model, 'rb'))

def textPreprocess(text):
    X_processed=[]
    for item in text:
        item= re.sub('[^a-zA-Z]', ' ', item)
        item=item.rstrip()
        item = item.lower()
        item = item.split()
        ps = PorterStemmer()
        item = [ps.stem(word) for word in item]
        item = ' '.join(item)
        X_processed.append(item)
    return X_processed

def sentimentAnalyzer(ticker):
    newNews=news(ticker)
    newDict=newNews['news']
    newsTitles=[]
    for item in newDict:
        temp=item['title']
        newsTitles.append(temp)
    newsTitlesPreprocess=textPreprocess(newsTitles)
    cv2=CountVectorizer(max_features=250)
    newsSparseMatrix=cv2.fit_transform(newsTitlesPreprocess).toarray()
    y_pred_news=loaded_model.predict(newsSparseMatrix)
    return y_pred_news 