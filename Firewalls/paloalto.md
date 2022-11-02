# Palo Alto Firewall Integration

Tested on:
- Firewall 9.1.X
- Panorama 10.1.X

## Setup

### Download AWS CA Cert & Upload

1. Download the AWS Starfield cert here: https://ssl-tools.net/certificates/ad7e1c28b064ef8f6003402014c3d0e3370eb58a.pem
2. Login to the FW and go to the certificate store
3. Upload the certificate, click on the cert, and check `Trusted Root CA`

### Panorama
1. In Panorama: Click on device in the top toolbar, and then on the left hand side certificate management --> certificates
2. Make sure the appropriate template is selected for the firewall that you want to push to (on the top toolbar)
3. On the bottom toolbar, click import, choose certificate, give it a name - use PEM for file format
4. Manually click on the starfield cert and check Trusted Root CA, click ok
5. Click certificate profile, on bottom left click add
6. Click add and select the starfield cert and click ok


### Create EDL

1. Go to objects --> External dynamic lists
2. Add give it a name, click Shared (if pushing to multiple firewalls)
- type: `IP List` 
- url: `https://api.threatanalysis.io/integrations/all/30d/txt?filter=ip`
- Certificate profile: select cert name `name`
- client auth
- user: user
- password: `api key`
- Check for updates: `daily`
3. Repeat steps 1 & 2 but this time we will add the domain list, everything stays the same except:
- type: `URL List`
- url: `https://api.threatanalysis.io/integrations/all/30d/txt?filter=domain`

### Create Policies

1. Click on policies
2. Add to your current blocklist policy and add EDL (block in destination)
3. Drop or deny rules

### Submit changes!

Commit and push, if local, do a commit

### Troubleshooting

Here are some commands that can help you troubleshoot the connection should you run into any issues

This will show how many valid/invalid entries got pulled

```
request system external-list show type ip name <EDL-Name>
```
This will show if the EDL is valid and when the last refresh was done   

```
request system external-list stats type ip name <EDL-Name>
```


To do a manual refresh of the EDL run the below command:
```
request system external-list refresh type ip name <EDL-Name>
```

You can check the progress of the EDL refresh by running the below commands after the manual refresh:
```
show jobs all
```
Copy the job ID shown for the EDLRefresh job
```
show jobs id <job-id>
```