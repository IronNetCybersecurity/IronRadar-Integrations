# Checkpoint Firewall Integration

Note: Your appliance must be on version R81.20 for custom intelligence feeds to work correctly.

## Setup - GUI

1. Open your CheckPoint SmartConsole and login
2. Open `SECURITY POLICIES` --> `Threat Prevention` --> Under `Custom Policy Tools` --> click on `Indicators`
3. On the top middle, click on the "star" like icon and click `New IOC Feed`
4. Use the following settings below:
- Name: `IronRadar_IP`
- Action: `Prevent`
- Feed URL: `https://api.threatanalysis.io/integrations/all/30d/csv?header=none&filter=ip`
- Feed Parsing:
  - Format: `Custom CSV`
  - Data Type: `IP Address`
  - Data Column: `1`
  - Delimeter: `Comma (,)`
- Additional Columnns:
  - Comment Column: `5`
  - Name Column: `4`
  - Severity Column: Leave blank
  - Confidence Column: `6`
- Use gateway proxy for connection: (depends on your set up)
- Authentication:
  - Username: `user`
  - Password: `API KEY HERE`
5. Finally, click `Test Feed` at the bottom of this prompt, if successful click okay and let's create the next feed. Otherwise, take a look at your settings above or reach out to our team for assistance. 
6. Do the same for the domain feed, but alter these two settings below:
- Name: `IronRadar_domain`
- Feed URL: `https://api.threatanalysis.io/integrations/all/30d/csv?header=none&filter=domain`
- Data Type: `Domain`
7. Click test feed to ensure your firewall pulled the indicators correctly.
8. Click ok, then click `publish` at the very top to commit these changes. Then in the top left, click on `Install Policy` to then push these policies to your firewall.
8. Both feeds will now ingest IronRadar IOCs!


## Troubleshooting Tips

1. SSH into your firewall
2. Escalate to Expert by executing the command `expert` and typing in your password.
3. Copy and paste the following commands into the CLI.

For additional commands: https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk132193

See which feeds are installed on your device:

```
ioc_feeds show
```
If installed correctly, this command should provide the following output: 
```
Feed Name: IronRadar_Domain
Feed is Active
File will be fetched via HTTPS
Resource: https://api.threatanalysis.io/integrations/all/30d/csv?header=none&filter=domain
Action: Prevent
Proxy:
User Name: user
Feed is centrally managed


Feed Name: IronRadar_IP
Feed is Active
File will be fetched via HTTPS
Resource: https://api.threatanalysis.io/integrations/all/30d/csv?header=none&filter=ip
Action: Prevent
Proxy:
User Name: user
Feed is centrally managed
```

You can force pull the indicators by running:
```
$FWDIR/bin/ioc_feeder -d -f
```

To further check that the indicators actually pulled onto the device, check the logs located here:
```
cd $FWDIR/external_ioc/
```