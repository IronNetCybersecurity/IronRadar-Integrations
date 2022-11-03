# NetWitness Integration

## Setup

1. Login to NetWitness UI, click on configure, custom feeds
2. Choose add new and choose custom feeds
3. Fill in the information with the following below: (we will do this step twice, one for IPs and again for domains)
- Feed type: `CSV`
- Feed Task Type: `Recurring`
- Name: `IronRadar - IPs`
- URL: `https://api.threatanalysis.io/integrations/all/30d/csv?header=none&filter=ip`
- Auth: Check authenticated
- User Name: `user`
- Password: `IronRadar API KEY`
- Recur Every: `1 Day`
4. Click next and then choose your decoded on the next screen
5. Map the columns with the correct attributes below:
- Type: `IP`
- Index Column: `1`
- 2: `port`
- 3: `time`
- 4: `threat.desc`
- 5: `threat.category`
- 6: `confidence`
- 7: `TLP`
- 8: `type` #or ignore
6. Click next and then finish. The feed should begin to pull in within a minute
7. Finally, repeat these steps for the IronRadar domain only feed. Here are the settings that will change
8. In step 3, change these settings:
- Name: `IronRadar - Domainss`
- URL: `https://api.threatanalysis.io/integrations/all/30d/csv?header=none&filter=domain`
9. In step 5, change the following:
- Type: `Non IP`
- Callback Keys: `alias.host` and `domain`
10. Now you should be pulling in both IP and domain indicators