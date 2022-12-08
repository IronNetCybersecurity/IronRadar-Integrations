# Threat Types

We created threat types to help provide additional context surrounding an indicator and its purpose ina  threat actor's infrastructure deployment. As we continue to expand our detections outside of simply just command and control (C2) servers, we developed a framework for contextualizing the specific threat and its puropse. This format uses dot-notation and attempts to closely align it's definitions using the [MITRE ATT&CK Framework](https://attack.mitre.org/). Below is an example for the format:

<MITRE ATT&CK>.<protocol | property>.<property>+

*Examples:*
- c2.http.address
- c2.http.listener
- c2.http.management
- c2.http.redirector
- c2.http.header.host
- c2.https.listener
- c2.tls.listener
- c2.tcp.listener
- malware.stager.md5
- malware.stager.sha1
- malware.stager.sha256
- recon.http.management

## Definitions

| Term | Type | Definition| 
| ------------- | ------------- | ------------- |
| C2 | MITRE ATT&CK Tactic | MITRE ATT&CK Tactic where the adversary is trying to communicate with compromised systems to control them. |
| Recon | MITRE ATT&CK Tactic | MITRE ATT&CK Tactic the adversary is trying to gather information they can use to plan future operations |
| Malware | MITRE ATT&CK Term | Commercial, custom closed source, or open source software intended to be used for malicious purposes by adversaries |
| Address | Infrastructure Property | The IP or domain of the host |
| Management | Infrastructure Property | The interface used to control a framework |
| Redirector | Infrastructure Property | A service that accepts connections and forwards them to another location |
| Header | Infrastructure Property | The field of an HTTP request that passes additional context and metadata about the request or response |
| Host | Infrastructure Property | The domain name of the server and the tcp port on which the server is listening on |
| Listener | Infrastructure Property | The indicator of the component of the C2 that is being used to communicate with the payload |



