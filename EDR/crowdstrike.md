# Crowdstrike Integration

## Automatic Upload (CSV)

1. Login to your Crowdstrike instance and create an API key for this script by going to the menu and click on `Support and resources` --> `API Clients and Keys` (you must have admin rights to create an API key)
2. Click `Add new API client` and enter the following:
- Name: `IronRadar`
- Description: `API key for IronRadar script.`
- Permissions:

| API Scopes | Read | Write | 
| ------------- | ------------- | ------------- |
| IOC Management | :white_check_mark:  | :white_check_mark: | 
| IOCs (Indicators of Compromise)  | :white_check_mark:  | :white_check_mark: |

3. Copy the [Crowdstrike directory](./crowdstrike_files)  to the host that you want to run the script on
4. Rename then .env.sample file to .env and edit the file to enter in your IronRadar API key, your Falcon Client ID and Secret
5. Then run the script! You should now see IOCs in your Falcon instance
```
python3 crowdstrike.py
```

### Troubleshooting

- For any issues ingesting IOCs into Crowdstrike Falcon, take a look at the audit_log.txt produced by the script
- For any issues grabbing indicators from IronRadar, the script will output to your terminal

## Manual Upload (TXT)

1. Login to your Crowdstrike instance
2. Click on the menu icon in the top left, `Endpoint security`--> and under configure click `IOC management`
3. Click on the 3 dots menu to the right of `Export` and click either `Add domains` or `Add IP addresses`
4. Upload a txt file for your respective indicators
5. Fill out the additional details for each of the fields and then click add!