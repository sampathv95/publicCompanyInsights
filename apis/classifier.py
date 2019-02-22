import numpy as np
import pandas as pd
import re
import sklearn
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import intrinio
import requests
import news
from news import news
import os
import pickle

dirname = os.path.dirname(__file__)
yelp = os.path.join(dirname, '../Datasets/yelp_labelled.csv')  
imdb = os.path.join(dirname, '../Datasets/imdb_labelled.csv')
amazon = os.path.join(dirname, '../Datasets/amazon_cells_labelled.csv')
                
X=pd.read_csv(yelp).iloc[:, 0].tolist()+pd.read_csv(imdb).iloc[:, 0].tolist()+pd.read_csv(amazon).iloc[:, 0].tolist()

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
X_processed=textPreprocess(X)
            
y=[]
y1=pd.read_csv(yelp).iloc[:, 1].tolist()
y=y1
y2=pd.read_csv(imdb).iloc[:, 1].tolist()
y=y+y2
y3=pd.read_csv(amazon).iloc[:, 1].tolist()
y=y+y3
y= np.array(y)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 250)
sparse_matrix= cv.fit_transform(X_processed).toarray()

from sklearn.svm import SVC
classifier_svm=SVC(kernel='linear', random_state=0)
classifier_svm.fit(sparse_matrix, y)

filename = 'Pickled_model.sav'
pickle.dump(classifier_svm, open(filename,'wb'))






