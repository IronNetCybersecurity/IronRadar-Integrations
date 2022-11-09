# Fortinet Firewall Integration

## Setup

1. Login to the firewall
2. Navigate to `Security Fabric` --> `External Connectors` --> `Create New` --> and under `Threat Feeds` click `IP Address`
3. Fill out the form using the details below:
- Name: `IronRadar - IP`
- Update Method: `External Feed`
- URI of external resource: `https://api.threatanalysis.io/integrations/all/30d/txt?filter=ip`
- HTTP basic authentication: Enabled
- Username: `user`
- Password: `API Key HERE`
- Refresh rate: `1440`
4. Repeat the same steps above, execept change the following fields:
- Name: `IronRadar - Domain`
- Update: `https://api.threatanalysis.io/integrations/all/30d/txt?filter=domain`