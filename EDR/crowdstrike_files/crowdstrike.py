#   Make sure to change the API Key
#   Alter the url if you only want to pull a specific C2 framework or if you want to pull a different timeframe
#   Docs -- https://api.threatanalysis.io/prod/docs/index.html

import os
import requests
import pandas as pd
from falconpy import IOC
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

    falcon = IOC(client_id=os.getenv("FALCON_CLIENT_ID"),client_secret=os.getenv("FALCON_CLIENT_SECRET"))
    df = pd.read_csv("ironradar.csv", usecols = ['indicator','threat','confidence','tlp', 'type'])
    df = df.drop_duplicates(subset='indicator', keep="first")
    num_indicators = len(df)

    print(f"Loading IOCs from: {os.getcwd()}/ironradar.csv into Crowdstrike")

    # global settings
    platform_list = os.getenv("platform_list")

    # audit_log
    audit_log = open("audit_log.txt", "w")
    audit_log.write("# Audit log for finding issues with IOC ingestion to Crowdstrike")
    audit_log.close()

    count = 0 
    while count < num_indicators:
        if df['type'][count] == 'ipv4-addr':
            type = 'ipv4'
            expiration_date = (date.today() + timedelta(days=90)).strftime('%Y-%m-%dT%H:%M:%SZ')
        elif df['type'][count] == 'domain-name':
            type = 'domain'
            expiration_date = (date.today() + timedelta(days=180)).strftime('%Y-%m-%dT%H:%M:%SZ')

        response = falcon.indicator_create(action="detect",
                                applied_globally=True,
                                description=f"Indicator associated with {df['threat'][count]} | Confidence: {df['confidence'][count]} | TLP: {df['tlp'][count]}",
                                expiration=expiration_date,
                                ignore_warnings=True,
                                platforms=platform_list,
                                severity="HIGH",
                                source="IronRadar",
                                tags = ['IronRadar',f"{df['threat'][count]}"],
                                type=type,
                                value=f"{df['indicator'][count]}"
                                )
        audit_log = open("audit_log.txt", "a")
        audit_log.write(f'\n {response}')
        audit_log.close()

        count += 1

    print(f"Completed loading IOCs into Crowdstrike")

elif r.status_code == 400:
    print('Check your url, docs: https://api.threatanalysis.io/prod/docs/index.html')
elif r.status_code == 403:
    print('Unauthorized -- check API key')