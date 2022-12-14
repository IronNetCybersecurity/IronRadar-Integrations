#   Make sure to change the API Key
#   Alter the url if you only want to pull a specific C2 framework or if you want to pull a different timeframe
#   Docs -- https://api.threatanalysis.io/prod/docs/index.html

import os
import requests
import pandas as pd

from management.mgmtsdk_v2_1.endpoints import THREAT_INTELLIGENCE
from management.mgmtsdk_v2_1.mgmt import Management
from management.mgmtsdk_v2_1.entities import threat_intelligence
from dotenv import load_dotenv
from datetime import timedelta, date

# loads environment variables from .env
load_dotenv()

headers = {'X-API-KEY': f'{os.getenv("api_key")}'}
url = "https://api.threatanalysis.io/prod/all/1d/csv"

print('Making API Request')
r = requests.get(url, headers=headers)

if r.status_code == 200:
    print('Connection successful')
    with open('ironradar.csv', 'wb') as f:
        f.write(r.content)
    print(f'file location: {os.getcwd()}/ironradar.csv')

    df = pd.read_csv("ironradar.csv", usecols = ['indicator','threat','confidence','tlp', 'type'])
    df = df.drop_duplicates(subset='indicator', keep="first")
    df.index = pd.RangeIndex(len(df))
    num_indicators = len(df)

    print(f"Loading IOCs from: {os.getcwd()}/ironradar.csv into SentinelOne")

    count = 0 
    while count < num_indicators:
        if df['type'][count] == 'ipv4-addr':
            ioc_type = 'IPV4'
            expiration_date = (date.today() + timedelta(days=90)).strftime('%Y-%m-%dT%H:%M:%SZ')
        elif df['type'][count] == 'domain-name':
            ioc_type = 'DNS'
            expiration_date = (date.today() + timedelta(days=180)).strftime('%Y-%m-%dT%H:%M:%SZ')

        newti = threat_intelligence.Ioc(randomize_empty=False)
        newti.__dict__.update(
            {
                "source": "IronRadar",
                "type": ioc_type,
                "description": f"Indicator associated with {df['threat'][count]} | Confidence: {df['confidence'][count]} | TLP: {df['tlp'][count]}",
                "value": f"{df['indicator'][count]}",
                "validUntil" : expiration_date,
                "method": "EQUALS"
            }
        )
        tiitems.append(newti)

        count += 1

    con = Management(f'{os.getenv("portal_url")}', api_token=f'{os.getenv("api_token")}')
    
    iocpost = {
        "filter": {
            "accountIds": [f'{os.getenv("account_id")}']      
        },
        "data": tidata
    }

    addti = con.client.post(endpoint=THREAT_INTELLIGENCE, payload=iocpost)
    if addti.status_code != 200:
        print("Failed to create/update IOC, response_code: {}".format(addti.status_code))
        print(f"Error: {addti.errors}")
    else:
        print("Completed loading IOCs into Crowdstrike")

elif r.status_code == 400:
    print('Check your url, docs: https://api.threatanalysis.io/prod/docs/index.html')
elif r.status_code == 403:
    print('Unauthorized -- check API key')