import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())



app_key = "your appkey"
app_secret = "your app secret"
refresh_token = "your refresh token"


data = {'refresh_token': refresh_token, 'grant_type': 'refresh_token'}

r = requests.post('https://api.dropbox.com/oauth2/token', data=data,
auth = HTTPBasicAuth(app_key, app_secret))
result = r.json()
result = result["access_token"]
def get_dropbox_access_token():
    return result
