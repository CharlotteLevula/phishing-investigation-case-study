# Sanitized indicators of compromise (IOCs)

**Defanged for publication.** These values are research indicators, not attribution claims. Do not click or browse suspicious sites.

| Type | Value | Context |
| --- | --- | --- |
| Domain | `omaverossa-suomii[.]com` | Email-linked phishing landing page |
| Domain | `i-kuuleminen-kela[.]com` | Related-looking suspicious site; operator link unconfirmed |
| Email sender | `no-responder@banango[.]app` | Authenticated sending domain; not proof of account owner involvement |
| Domain | `em2648.banango[.]app` | Envelope return path |
| Domain | `url7399.banango[.]app` | Tracking host |
| IP | `149.72.243.42` | SendGrid relay, not attacker IP |
| IP | `172.67.176.129` | Cloudflare edge observation |
| IP | `172.67.201.47` | Cloudflare edge observation |
| IP | `104.21.44.162` | Cloudflare edge observation |
| SHA-256 | `94a1f26835211ad77427248fc761e3bab7d8e406344100d0b1d848b7ddcb9bb0` | Reusable DisableDevtool library, not necessarily malicious by itself |

**Publication note:** The SendGrid sender domain may belong to a legitimate third party whose infrastructure was abused. Avoid labeling its operator as malicious without additional evidence.
