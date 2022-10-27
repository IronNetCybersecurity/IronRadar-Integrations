# XSOAR Integration

## Setup

1. Login to your instance of XSOAR and in the bottom left click on the cube icon that is the marketplace
2. Browse for the package called `CSV Feeds` by Cortex XSOAR and install it
3. Once installed, click on the settings icon in the bottom left, click on Integrations, and then search for `CSV Feed`, you should now see the integration
4. Click on `Add instance` and add the following:
- Name: `IronRadar`
- Indicator Selection: `Fetches indicators`
- Indicator Reputation: `Malicious`
- Source Reliability: `A - Completely Reliable`
- Traffic Light Protocol Color: `Amber`
- Indicator Expiration Method: `Time Interval` or `Indicator Type`
- Indicator Expiration Method (optional): `90 days`
- Feed Fetch Interval: `1 day`
- Check: `Auto detect indicator type`
- URL: `https://api.threatanalysis.io/prod/all/1d/csv?header=comment`
- Username: `_header:x-api-key`
- Password: `API KEY HERE`
- Request Timeout: `20`
- Ignore Regex: `^#`
- Field Names: `value,port,last_seen,threat,threat_type,confidence,tlp,type`
- Delimeter: `,`

5. Run test, to ensure connection is succesful, and click save
6. Once indicators are pulled, open the window back up by clicking the settings icon and click on `Mapper`
7. On the top, select `Pull from instance` for Get Data, and for select instance, click on the dropdown and choose `IronRadar CSVFeed`
8. On Indicator Mapping, select `Common Mapping` and set the following settings:
- Confidence: `confidence`
- Feed Related Indicators: `value`
- Last Seen By Source: `last_seen`
- Tags: `threat`
- Threat Types: `threat_type`
- Traffic Light Protocol: `tlp`
9. In the text box in the type left, type `IronRadar` and then click `Save Version` in the top left and go back to settings -> Integrations -> and click on the settings icon for IronRadar
10. Set the Mapper to `IronRadar`
11. Indicators should begin ingesting and the columns will be appropriately mapped!