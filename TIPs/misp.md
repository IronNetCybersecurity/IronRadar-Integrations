# MISP Integration

## Setup

1. Login to your MISP instance
2. Hover over 'Sync Actions' click 'List Feeds'
3. Click on 'Add Feed'
4. Enter in details:
- Name: `IronRadar`
- Provider: `IronNet Cybersecurity`
- Input Source: `Network`
- URL: `https://api.threatanalysis.io/integrations/misp`
- Source Format: `MISP Feed`
- Headers: `x-api-key: api_key_here`
5. Click submit
6. Under actions, for the IronRadar feed, click on the magnifying glass icon to view the indicators in order to ensure that they pulled properly
