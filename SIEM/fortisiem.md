# FortiSIEM Integration

## Setup

1. Login to your FortiSIEM instance and browse to `Resources`
2. On the left hand side menu, click `Malware IPs` and then click the `+` icon above the menu to add a new group
3. Name the group `IronRadar - IPs` and click save
4. Expand `Malware IPs`, click on `IronRadar IPs` and then in the top menu, click `more` --> `update` and select `Update via API`
5. Click on the pencil icon and fill in the settings with the following below:
- URL: `https://api.threatanalysis.io/integrations/all/30d/csv?filter=ip`
- User Name: `user`
- Password: `API KEY HERE`
- Data Update: `Full`
- Data Mapping / Mapped Field:
    - `Low IP` - `1`
    - `Last Seen` - `3`
    - `Malware Type` - `4`
    - `Description` - `5`
    - `Confidence` - `6`
6. Click save, click `+` on schedule, and you can set this to be whatever time you'd like. Remember, the indicators are only refreshed every 24 hours. We're going to set ours to daily, and to refresh at 0400 ET.
7. Now we're going to repeat the steps above except we're going to add a feed under `Malware Domains`. Add a new group, and name it: `IronRadar - Domains`
8. Expand `Malware Domains`, click on `IronRadar - Domains` and then add a API feed. Add the following API settings:
- URL: `https://api.threatanalysis.io/integrations/all/30d/csv?filter=domain`
- User Name: `user`
- Password: `API KEY HERE`
- Data Update: `Full`
- Data Mapping / Mapped Field:
    - `Domain Name` - `1`
    - `Last Seen` - `3`
    - `Malware Type` - `4`
    - `Description` - `5`
    - `Confidence` - `6`
9. Click save, and then add the same schedule as you did for the IP feed.
10. Now you should see indicators from both feeds!



