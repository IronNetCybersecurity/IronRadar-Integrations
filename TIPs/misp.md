# MISP Integration

MISP Feed format coming soon!

## Setup (TXT)

1. Login to your MISP instance
2. Hover over 'sync actions' click 'list feeds'
3. Click on 'add feed'
4. Enter in details:
- Name: `IronRadar`
- Provider: `IronNet Cybersecurity`
- Input Source: `Network`
- URL: `https://api.threatanalysis.io/prod/all/1d/txt`
- Source Format: `Freetext Parsed Feed`
- Headers: `x-api-key: api_key_here`
5. Click submit
6. Under actions, for the IronRadar feed, click on the magnifying glass icon to view the indicators in order to ensure that they pulled properly