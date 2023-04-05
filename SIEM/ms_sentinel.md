# Microsoft Sentinel Integration

## Setup

1. Open Microsoft Sentinel in the Azure portal
2. Click on your analytic workspace
3. Under configuration, click on data connectors
4. Search for “taxi” and select the `Threat Intelligence - TAXII` connector by Microsoft
5. Click open connector page and enter the following under configuration:
- Friendly Name: `IronRadar`
- URL: `https://opencti.ironradar.threatanalysis.io/taxii2/root/`
- Collection ID: `5570a9ec-bd1d-436f-b8eb-1e4ddd307bd0`
- User Name: `USERNAME HERE`
- Password: `PASSWORD HERE`
- Import Indicators: `At most one month old`
- Polling: `Once a day`
6. Click add!