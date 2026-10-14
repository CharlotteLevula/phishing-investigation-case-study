# Phishing Investigation: Finnish Public-Service Impersonation

![Focus](https://img.shields.io/badge/Focus-Threat%20Intelligence-informational) ![Approach](https://img.shields.io/badge/Method-Passive%20Analysis-green) ![Status](https://img.shields.io/badge/Attribution-Unconfirmed-lightgrey)

> A defensive case study based on a phishing email received in October 2026. All published indicators are defanged, and sensitive/raw evidence is excluded.

## Executive summary

On **11 October 2026**, a phishing email impersonating Finland's **Kanta.fi** healthcare service was received. The message linked to a fraudulent public-service authentication page on `omaverossa-suomii[.]com`. A second suspicious site, `i-kuuleminen-kela[.]com`, was investigated for technical similarities.

Email headers show delivery through **SendGrid** infrastructure, with SPF, DKIM and DMARC passing for `banango.app` — **not** for the impersonated Kanta.fi service. This demonstrates that authentication success is not evidence of message legitimacy.

Two supplied HTML captures were statically decoded. Their decoded pages share **96.44% character-sequence similarity** (Python `difflib.SequenceMatcher`, `autojunk=False`) and identical observed `conversation`, `tid`, `pid` and `tag` values. Both supplied JavaScript captures of `devtool.js` have the same SHA-256 digest. These findings support **reuse of a shared template or kit**, but **do not establish a common operator, identity, or location**.

## Investigation scope

- Email header and routing analysis
- Passive domain/infrastructure observations from archived scan reports
- Static HTML deobfuscation and JavaScript comparison
- Evidence-based assessment of possible campaign linkage
- Responsible reporting and limitations

**No live phishing pages were accessed as part of this repository build. No credentials were entered, and no malicious code was executed.**

## Evidence highlights

| Observation | Assessment |
| --- | --- |
| Sender shown as `no-responder@banango[.]app` | Authenticated sending domain, not proof of sender's identity |
| Sending relay `149.72.243.42` | SendGrid relay; **not** the attacker's origin IP |
| SPF/DKIM/DMARC pass for `banango.app` | Authentication did not validate the Kanta impersonation |
| Decoded HTML similarity: **96.44%** | Strong template similarity; not a probabilistic attribution score |
| Matching `conversation`, `tid`, `pid`, `tag` | Shared values observed; meaning/uniqueness unverified |
| Identical DisableDevtool library | Shared third-party library; not by itself evidence of same actor |
| One extra bank option in one HTML capture | Pages are similar but not identical |

## Repository guide

- [Email forensics](analysis/email-header-analysis.md)
- [Infrastructure and OSINT](analysis/infrastructure-analysis.md)
- [HTML and JavaScript comparison](analysis/phishing-kit-comparison.md)
- [Timeline](analysis/timeline.md)
- [Defanged indicators](evidence/indicators.md)
- [Reproducible local analysis script](tools/compare_html.py)

## Reproduce the comparison (private evidence only)

Keep original samples **outside the public repository**. Use the local comparison script on the two original HTML capture files:

```bash
python tools/compare_html.py /path/to/sample_a.md /path/to/sample_b.md
```

The script **does not execute JavaScript or make network requests**. It extracts a specific ROT13 → Base64 → URL-decoding wrapper observed in these captures, computes hashes and similarity, and prints a minimal comparison.

## Responsible disclosure

An incident report was prepared for Finland's National Cyber Security Centre (NCSC-FI), including the original email as an attachment. **Submission/receipt status should be updated only after independently confirmed.** Attempts to email the SendGrid abuse address from Gmail were blocked by Gmail's outgoing abuse controls. No investigation outcome or attribution is claimed.

## Ethical and analytical boundaries

- No victim identifiers, personal email addresses, full original headers, raw `.eml` files, active hyperlinks to phishing sites, payloads, or executable phishing code are published.
- IP geolocation of CDN or email relay infrastructure is **not** attacker geolocation.
- Similar templates may be sold, copied or reused by unrelated actors.
- The supplied `.mobileconfig` attachment content was unavailable; the recovered 85-byte file was a security replacement notice, **not** the original payload.
- No credential exfiltration was demonstrated from the static landing-page HTML alone.

## Sources

- [urlscan report: OmaVero-themed domain](https://urlscan.io/result/01a13950-28b4-734e-a0a6-2a3bad45c506/)
- [urlscan report: Kela-themed domain](https://urlscan.io/result/01a130af-61e8-7286-bb17-4cc860d9ca0d/)
- Original private email and HTML/JavaScript samples (not distributed)

## Author note

Independent defensive research case study. This repository is not affiliated with Kanta, Kela, Suomi.fi, Banango, SendGrid or any other named organization.
