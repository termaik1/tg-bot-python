import requests

def get_cat():
    r = requests.get('http://thecatapi.com/api/images/get?format=src')
    url = r.url
    return url