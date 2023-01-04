# SentinelOne Integration [Beta]

** Note: The threat intelligence feature for SentinelOne is not GA yet. If you want to enable this feature, reach out to your account team to have it enabled.

### Prep Python Env.

In order to utilize this tool you will need to install SentinelOne's Management SDK.

1. Login to your SentinelOne instance, and in the top right, click on `Help` --> `API Doc`
2. In the top right, click on `Management SDK`
3. Download the `sentinel-mgmt-sdk.tar.gz` file and then run pip to install the SDK

## Automatic Upload (CSV)

1. Login to your SentinelOne instance, you will need to get your account ID and your API key.
2. For your account ID, click on `sentinels` on the left hand side menu, and then click on `account info` on the top menu. Under the name of your company, you should see account ID, copy and paste that into the .env file.
3. For your API Key, click on `settings` on the left hand side menu, and then click on `users` on the top menu. Click on your user, and then click on `options` --> `API Token Operations` and generate your API Key and copy and paste it into the .env file. You can also create a specific user that is just for IronRadar / API operations.
4. If you haven't done so yet, copy and paste your IronRadar API key into the .env file.
5. Finally, copy and paste the url of your SentinelOne instance into the .env. Example: `https://usea1-partners.sentinelone.net`
6. Once all of the values in .env are set, let's run the python script:
```
python3 sentinelone.py
```
7. At the end of the script, it will print out how many IronRadar indicators are in SentinelOne!


## Set Star Rules for IronRadar Detection

1. In your SentinelOne instance, click on `visibility` on the left hand side menu, and then click on `Star Custom Rules` on the top menu.
2. Click on `New Rule` and let's create a rule with the following options:
- Rule Name: `IronRadar Detection`
- Description: `IronRadar threat intelligence source that proactively detects adversary infrastructure`
- Rule Severity: `High`
- Rule Type: `Permanent`
3. Click next and copy and paste the query below:
```
TIIndicatorSource = "IronRadar"
```
4. For active response, check `Treat as a threat` and then select either policy that best fits your needs!
5. Click next, review the custom rule, and then activate. If SentinelOne detects traffic to an IronRadar indicator, it will now alert!
