# Checkpoint Firewall Integration

Note: this integration was tested on version R81 and is still undergoing testing

## Setup - GUI

1. Open your CheckPoint SmartConsole and login
2. Open `SECURITY POLICIES` --> `Threat Prevention` --> Under `Custom Policy Tools` --> click on `Indicators`
3. On the top middle, click on the "star" like icon and click `External IOC feed`
4. Use the following settings below:
- Name: `IronRadar_IP`
- Active: :white_check_mark:
- Feed URL: `https://api.threatanalysis.io/integrations/all/30d/txt?filter=ip`
- Action: `Prevent`
- Use gateway proxy for connection: (depends on your set up)
- Authentication:
  - Username: `<API KEY HERE>`
  - Password: `Password`
5. Click test connectivity, if that works, then click ok! Otherwise, alter your settings above or check your API key.
6. Do the same for the domain feed, but alter these two settings below:
- Name: `IronRadar_domain`
- Feed URL: `https://api.threatanalysis.io/integrations/all/30d/txt?filter=domain`
7. Test and click ok
8. Both feeds will now ingest IOCs


## Setup - CLI

1. SSH into your firewall
2. Copy and paste the following commands into the CLI.

NOTE: Make sure to enter your API key after username: `<API KEY>`

- Add IP Feed:

```
ioc_feeds add --feed_name ironradar_ip--transport https --resource "https://api.threatanalysis.io/integrations/all/30d/txt?filter=ip" --user_name <API KEY> --format [value:1,type:ip]
```
- Add Domain Feed:
```
ioc_feeds add --feed_name ironradar_domain --transport https --resource "https://api.threatanalysis.io/integrations/all/30d/txt?filter=domain" --user_name <API KEY> --format [value:1,type:domain]
```

3. When prompted for a password via the CLI, you can just enter `password` as the server ignores the password field.

4. You can force pull the indicators by running:
```
$FWDIR/bin/ioc_feeder -d -f
```

5. To further check that the indicators actually pulled onto the device, check the logs located here:
```
cd $FWDIR/external_ioc/
```