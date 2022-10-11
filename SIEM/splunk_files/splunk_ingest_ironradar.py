#   Make sure to change the API Key
#   Alter the url if you only want to pull a specific C2 framework or if you want to pull a different timeframe
#   Docs -- https://api.threatanalysis.io/prod/docs/index.html

import requests

api_key = "ENTER API KEY HERE"
headers = {'X-API-KEY': f'{api_key}'}
url = "https://api.threatanalysis.io/prod/all/1d/csv"

r = requests.get(url, headers=headers)

print(r.text)