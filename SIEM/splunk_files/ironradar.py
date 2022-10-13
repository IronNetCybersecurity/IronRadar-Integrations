#   Make sure to change the API Key
#   Alter the url if you only want to pull a specific C2 framework or if you want to pull a different timeframe
#   Docs -- https://api.threatanalysis.io/prod/docs/index.html

import os
import requests

api_key = "ENTER YOUR API KEY"
headers = {'X-API-KEY': f'{api_key}'}
url = "https://api.threatanalysis.io/prod/all/1d/csv"

print('Making API Request')
r = requests.get(url, headers=headers)

if r.status_code == 200:
    print('Connection successful')
    with open('ironradar.csv', 'wb') as f:
        f.write(r.content)
    print(f'file location: {os.getcwd()}/ironradar.csv')
elif r.status_code == 400:
    print('Check your url, docs: https://api.threatanalysis.io/prod/docs/index.html')
elif r.status_code == 403:
    print('Unauthorized -- check API key')