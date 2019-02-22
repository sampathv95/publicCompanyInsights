import numpy as np
import requests
import intrinio
def financialNumbers(ticker):
    fin_num={}
    fin_num['market_cap']=requests.get('https://api-v2.intrinio.com/companies/'+ticker+'/data_point/marketcap/number?api_key=OmFmMTIyOTQ1YjUyMTNiNmI0OWI0MTBhNjM2MDNjMDQw').json()
    fin_num['net_cash_flow_op']=requests.get('https://api-v2.intrinio.com/companies/'+ticker+'/data_point/netcashfromoperatingactivities/number?api_key=OmFmMTIyOTQ1YjUyMTNiNmI0OWI0MTBhNjM2MDNjMDQw').json()
    fin_num['net_ash_flow_fin']=requests.get('https://api-v2.intrinio.com/companies/'+ticker+'/data_point/netcashfromfinancingactivities/number?api_key=OmFmMTIyOTQ1YjUyMTNiNmI0OWI0MTBhNjM2MDNjMDQw').json()
    fin_num['net_cash_flow_inv']=requests.get('https://api-v2.intrinio.com/companies/'+ticker+'/data_point/netcashfrominvestingactivities/number?api_key=OmFmMTIyOTQ1YjUyMTNiNmI0OWI0MTBhNjM2MDNjMDQw').json()
    fin_num['last_year_revenue']=requests.get('https://api-v2.intrinio.com/companies/'+ticker+'/data_point/totalcostofrevenue/number?api_key=OmFmMTIyOTQ1YjUyMTNiNmI0OWI0MTBhNjM2MDNjMDQw').json()
    return fin_num
a=financialNumbers('AAPL')