# Tines Integration

## Setup

1. Log in to your Tines tenant and open a Story
2. Browse to the "Templates" section on the left and search for "IronRadar". You will see two integrations available:

- Pull IOCs from IronRadar
- Search for IOC in IronRadar

3. Drag and drop one of the integration groups into your story.

<img src="images/tines-templates.png" width=75% height=75%>

4. You will notice, to interact with the IronRadar API, you will need to add a credential to your Tines tenant called `IronRadar`. This should be set to the value of the API key provided when purchasing access to the service.

<img src="images/tines-ironradar-credential.png" width=25% height=25%>

5. When using the "Search" integration, a single argument called `indicator` is required and must be either a `domain` or `ip`.

<img src="images/tines-search-ioc.png" width=75% height=75%>

6. When using the "Pull IOCs" integration, you have all the options available to filter the results to just the IOC groups/types desired. For full API documentation, check out our [Swagger docs](https://api.threatanalysis.io/prod/docs/index.html#/) where you can test out queries live.

<img src="images/tines-pull-iocs.png" width=75% height=75%>
