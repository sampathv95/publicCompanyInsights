import numpy as np
import requests
import intrinio
def news(ticker):
    url = ('https://api-v2.intrinio.com/companies/'
               +ticker+'/news?api_key=OmFmMTIyOTQ1YjUyMTNiNmI0OWI0MTBhNjM2MDNjMDQw')
    response = requests.get(url).json()
    return response

