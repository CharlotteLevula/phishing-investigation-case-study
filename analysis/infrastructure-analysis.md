# Infrastructure and OSINT analysis

## Observed domains

| Defanged indicator | Observed role | Evidence source |
| --- | --- | --- |
| `omaverossa-suomii[.]com` | Fake Finnish public-service authentication landing page | Original email; urlscan |
| `i-kuuleminen-kela[.]com` | Kela-themed suspicious site | urlscan capture |
| `banango[.]app` | Authenticated sending domain | Original email headers |
| `em2648.banango[.]app` | Return-path domain | Original email headers |
| `url7399.banango[.]app` | Email open tracking | Original email body |

## Passive scan observations

Archived urlscan observations indicated Cloudflare-facing IPs (`172.67.176.129` for the OmaVero-themed host; `172.67.201.47` and `104.21.44.162` for the Kela-themed host). These are CDN edge addresses and **must not be interpreted as attacker location or origin-server IPs**. Scan observations are time-bound and may no longer reflect current DNS.

Both archived captures included similarly structured paths, CSS and bank-selection assets, plus `/cdn-static/js/devtool.js`. Resource similarity is evidence of common implementation patterns, not conclusive actor attribution.

## Attribution confidence

| Claim | Confidence | Why |
| --- | --- | --- |
| Email used SendGrid infrastructure | High | Received chain and authentication results |
| Landing pages share substantial template code | High | Static decoded HTML comparison |
| Both sites operated by one actor | Unknown | Shared kits can be reused independently |
| Attacker is located where Cloudflare or SendGrid IP geolocates | Unsupported | Shared provider infrastructure |
| `banango.app` owner knowingly sent the phishing email | Unsupported | Account misuse is plausible but unverified |

## Useful follow-up (for authorized investigators)

Provider-side SendGrid account and API activity logs, registrar records obtained through appropriate legal channels, and confirmed origin-server telemetry could improve attribution. Public data alone does not establish a named person or their physical location.
