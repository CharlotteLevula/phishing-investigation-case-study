# Static phishing-page comparison

## Method

Two locally supplied HTML captures were processed without opening the sites or executing embedded JavaScript. Each contained a wrapper that used ROT13-obfuscated JavaScript text and a Base64-encoded, URL-escaped HTML document. The script in `tools/compare_html.py` extracts and decodes that layer as **data**.

## Verified results

| Metric | HTML sample A | HTML sample B |
| --- | --- | --- |
| Decoded UTF-8 character count | 14,482 | 15,550 |
| SHA-256 of decoded HTML | `6662219cde555f6af64bfba68e2e803745093168bdd9cbf545959a19d5dc5d9b` | `dab060a5c84fd4a16bb4f3e18276150a5e0237a51c38eef1510a35b7ce21b0bd` |
| Page title | `Valitse tunnistustapa - Suomi.fi-tunnistus` | Same |
| Bank provider path variants | 7 | 8 |

**Decoded character-sequence similarity: 96.44%**, calculated with Python `difflib.SequenceMatcher(None, sample_a, sample_b, autojunk=False).ratio()`. This is a text similarity metric, **not** a statistical probability that the operators are the same.

Both samples contained identical observed parameter values:

- `conversation`: `e2s1`
- `tid`: `sg0sbeb8l9s50eem2j3mr2e5lk`
- `pid`: same 64-character value (redacted here; full value not needed for public presentation)
- `tag`: `2601240019e196`

One sample includes a `DANSKEBANK` provider path not observed in the other. The captured paths use names such as `NORDE` rather than a fully spelled-out `NORDEA`; this report preserves the literal observed path spelling.

## JavaScript library

Two supplied `devtool.js` captures had identical SHA-256 digest:

`94a1f26835211ad77427248fc761e3bab7d8e406344100d0b1d848b7ddcb9bb0`

The code corresponds to a minified **DisableDevtool v0.3.7** anti-inspection library. Its presence can deter casual browser inspection, but because it is reusable third-party code, identical hashes alone do not identify a shared operator. No credential-exfiltration mechanism was identified within this library.

## Limitations

No login interaction was performed; no downstream pages, POST requests, or collection endpoints were verified. Absence of a credential-submission form in the decoded landing-page snapshot does **not** establish that the broader flow is harmless. The two HTML files are designated sample A/B because the raw filenames alone do not independently prove which domain each sample originated from.
