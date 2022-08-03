from fastapi import FastAPI

app = FastAPI()
import requests

base_currency = 'BRL'
symbol = 'XAU%2CXAG%2CXPD%2CXPT%2CXRH'
endpoint = 'latest'
access_key = 'az0hyah4188pc9den3iw1l9pw1i1tq1o4e0etyp832dn7e5s11p942949a7e'



@app.get('/')
def home():
    resp = requests.get(
        'https://metals-api.com/api/' + endpoint + '?access_key=' + access_key + '&base=' + base_currency + '&symbols=' + symbol)
    response = resp.json()
    return response["rates"]