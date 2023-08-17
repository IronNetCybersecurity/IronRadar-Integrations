import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

#Use the redirect URL to create a token url
token_url = f'https://login.microsoftonline.com/{os.getenv("tenantId"}/oauth2/token'
token_data = {
 'grant_type': 'client_credentials',
 'client_id': os.getenv("clientId"),
 'client_secret': os.getenv("clientSecret"),
 'resource': 'https://graph.microsoft.com',
 'scope':'https://graph.microsoft.com',
}
token_r = requests.post(token_url, data=token_data)
token = token_r.json().get('access_token')

# Microsoft Graph Endpoints:
indicators_url = 'https://graph.microsoft.com/beta/security/tiIndicators'
submit_indicators = 'https://graph.microsoft.com/beta/security/tiIndicators/submitTiIndicators'

headers = {
 'Authorization': f'Bearer {token}'
}

#indicator_response_data = json.loads(requests.get(indicators_url, headers=headers).text)
#print(indicator_response_data['value'])


if r.status_code == 200:
    print('Connection successful')
    with open('ironradar.csv', 'wb') as f:
        f.write(r.content)
    print(f'file location: {os.getcwd()}/ironradar.csv')
    
    df = pd.read_csv("ironradar.csv", usecols = ['indicator','threat','confidence','tlp', 'type'])
    df = df.drop_duplicates(subset='indicator', keep="first")
    df.index = pd.RangeIndex(len(df))
    num_indicators = len(df)

    # Get current IronRadar Indicators
    #indicator_response_data = json.loads(requests.get(indicators_url, headers=headers).text)


    print(f"Loading IOCs from: {os.getcwd()}/ironradar.csv into Crowdstrike")

    # audit_log
    audit_log = open("audit_log.txt", "w")
    audit_log.write("# Audit log for finding issues with IOC ingestion to Microsoft Defender")
    audit_log.close()

    tiitems = []
    newti = {}

    count = 0 
    while count < num_indicators:
        if df['type'][count] == 'ipv4-addr':
            type = 'networkIPv4'
            expiration_date = (date.today() + timedelta(days=90)).strftime('%Y-%m-%dT%H:%M:%SZ')
        elif df['type'][count] == 'domain-name':
            type = 'domainName'
            expiration_date = (date.today() + timedelta(days=180)).strftime('%Y-%m-%dT%H:%M:%SZ')
        else
            continue

        tmpti = newti.copy()
        tmpti['action'] = 'block'
        tmpti['domainName'] = df['indicator'][count]
        tmpti['targetProduct'] = 'Microsoft Defender ATP'
        tmpti['description'] = f"Source: IronRadar | Threat: {df['threat'][count]} | Confidence: {df['confidence'][count]}"
        tmpti['threatType'] = 'C2'
        tmpti['tlpLevel'] = df['tlp'][count]
        tmpti['tags'] = ['ironradar']
        tiitems.append(tmpti)

        count += 1

    

    audit_log = open("audit_log.txt", "a")
    audit_log.write(f'\n {response}')
    audit_log.close()

    print(f"Completed loading IOCs into Microsoft Defender")

elif r.status_code == 400:
    print('Check your url, docs: https://api.threatanalysis.io/prod/docs/index.html')
elif r.status_code == 403:
    print('Unauthorized -- check API key')