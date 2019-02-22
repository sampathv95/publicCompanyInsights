import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
def earningCallData(ticker):
    if ticker=='OXY':
        url='https://finance.yahoo.com/news/edited-transcript-oxy-earnings-conference-225757092.html?.tsrc=rss'
    elif ticker=='EOG':
        url='https://finance.yahoo.com/news/edited-transcript-eog-earnings-conference-192941436.html'
    elif ticker=='PXD':
        url='https://finance.yahoo.com/news/edited-transcript-pxd-earnings-conference-223212862.html'
    elif ticker=='APA':
        url='https://finance.yahoo.com/news/edited-transcript-apa-ax-earnings-094517695.html'
    elif ticker=='APC':
        url='https://finance.yahoo.com/news/edited-transcript-apc-earnings-conference-235220786.html'
    else:
        url='https://finance.yahoo.com/news/edited-transcript-cop-earnings-conference-041452253.html'
    page=requests.get(url)
    soup = (BeautifulSoup(page.content, 'html.parser'))
    article_tag_to_string=str(soup.find_all('article'))
    string_split=article_tag_to_string.split('================================================================================')
    
    string_split_1=string_split[8]
    name_container=string_split_1.split('* ')
    name_container=name_container[1:len(name_container)]
    name_container_alternate=[]
    for i in range(len(name_container)):
        if (i%2==0):
            name_container_alternate.append(name_container[i])
    names=[]
    for name in name_container_alternate:
        temp=name.split()
        temp=temp[0:2]
        temp=' '.join(temp)
        temp=temp.replace('\"', '')
        names.append(temp)
    
    time_of_call=string_split[0]
    time_of_call=time_of_call.split('presentation')
    time_of_call=time_of_call[1]
    time_of_call=time_of_call.split('\"')
    time_of_call=time_of_call[0]
    return names, time_of_call
