# Palo Alto Firewall Integration

Tested on:
- Firewall 9.1.X
- Panorama 10.1.X

## Setup

### Download AWS CA Cert & Upload

1. Download the AWS Starfield cert here: https://ssl-tools.net/certificates/ad7e1c28b064ef8f6003402014c3d0e3370eb58a.pem
2. In Panorama: Click on device in the top toolbar, and then on the left hand side certificate management --> certificates
3. Make sure the appropriate template is selected for the firewall that you want to push to (on the top toolbar)
4. On the bottom toolbar, click import, choose certificate, give it a name - use PEM for file format
5. Manually click on the starfield cert and check Trusted Root CA, click ok
6. Click certificate profile, on bottom left click add
7. Click add and select the starfield cert and click ok

Note: If you are using a non-Panorama managed firewall, the steps are the same just without needing to specify a template

### Create EDL

1. Go to objects --> External dynamic lists
2. Add give it a name, click Shared (if pushing to multiple firewalls)
- type: `IP List` 
- url: `https://api.threatanalysis.io/integrations/all/30d/txt?filter=ip`
- Certificate profile: select the certificate profile created in the previous section
- client auth
- user: user
- password: `api key`
- Check for updates: `daily`
3. Repeat steps 1 & 2 but this time we will add the domain list, everything stays the same except:
- type: `URL List`
- url: `https://api.threatanalysis.io/integrations/all/30d/txt?filter=domain`

### Create Policies

1. Click on Policies
2. Create a new security policy and put the new IP EDL in the Source Address field (if wanting to block inbound connections from these IPs) OR put the new IP EDL in the Destination Address field (if wanting to block connections going TO these IPs)
3. For the URL EDL, you will want to create another security policy, placing the URL EDL in the URL Category field
4. Be sure to change the action to either Drop/Deny, and have these policies at the top of your security policies


### Submit changes!

Commit and push, if local, do a commit

## Troubleshooting

Here are some commands to run on the firewall that can help you troubleshoot the connection, should you run into any issues

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