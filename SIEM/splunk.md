# Splunk Integration

The easiest way to ingest data into splunk, is to take our ingest python script and to add it to your Splunk instance.

## Setup (Ingest via Script)

1. Download [splunk_ingest_ironradar.py](./splunk_files/splunk_ingest_ironradar.py)
2. Open the file, and add your API key to the variable `api_key`
3. Save the file and move the file to `$SPLUNK_HOME\bin\scripts\`
4. Login to your Splunk instance
5. In the top right, click settings, and under 'data' click on 'data inputs'
6. Click on scripts and then in the top right, 'new local script'
7. The following is our recommended settings - set the cron job to run daily in order to ingest our latest indicators:
![source settings](./splunk_files/source_settings_screenshot.png)
8. Proceed to the next page by clicking next and follow the settings below. In this step, you can either add our dataset to a current index or create a new index on this page. Our index is called `ironradar`
![input settings](./splunk_files/input_settings_screenshot.png)
9. Finally, click review and then submit! Now you can search the data in the index.