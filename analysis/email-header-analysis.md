# Email header analysis

## Evidence

The phishing email was received **11 October 2026, 16:45:14 UTC** (19:45:14 Finland local time, EEST). Display name: `tunnistaaOmakanta`; authenticated sender domain: `banango[.]app`.

| Field | Observed value | Interpretation |
| --- | --- | --- |
| SMTP relay IP | `149.72.243.42` | SendGrid outbound relay, not attacker origin |
| SMTP HELO | `wrqvfpnx.outbound-mail.sendgrid.net` | SendGrid outbound host |
| Envelope mail-from domain | `em2648.banango[.]app` | Authenticated bounce domain |
| DKIM `d=` | `banango[.]app` | Signature verified for this domain |
| SPF / DKIM / DMARC | pass / pass / pass | For `banango.app`, not for Kanta.fi |
| SendGrid SMTP ID | `T46qwEZ_TPqlaanaIlZIpQ` | Potentially useful to provider-side investigation |
| Message-ID | `<a0b2e050-5370-eb01-550b-69806cb21439@banango.app>` | Message correlation, not identity proof |
| Tracking host | `url7399.banango[.]app` | Open-tracking pixel host |
| Landing host | `omaverossa-suomii[.]com` | Impersonation link |

## Interpretation

Microsoft's receiving system reported authentication success. This supports that the message was transmitted using an authorized sending arrangement for the domain, **not** that the content was legitimate or the domain owner knowingly sent it. A compromised account, exposed API key, or other misuse are hypotheses, not confirmed facts.

A SendGrid `Received` line shows `127.0.0.1` before the provider's SMTP service. That loopback address cannot be used to infer the sender's public IP or location. Provider-side logs would be required for more precise origin attribution.

## Attachment limitation

The available `Update_TuQSig.mobileconfig` copy contained only an 85-byte security replacement notice. The original attachment was not available for analysis. No claim is made about its payload or behavior.

## Privacy

Recipient email address, full raw headers, message body and unique tracking-token values are withheld from this public repository.
