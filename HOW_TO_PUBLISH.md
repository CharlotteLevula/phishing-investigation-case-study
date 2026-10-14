# Publish on GitHub

1. Review README and reports for accuracy, especially disclosure status.
2. Create a new **public** repository named `phishing-investigation-case-study` on GitHub, without auto-generating README.
3. Extract this ZIP to your computer, open a terminal inside the extracted directory, then run:

```bash
git init
git add README.md LICENSE .gitignore HOW_TO_PUBLISH.md analysis evidence tools
git commit -m "Add defensive phishing investigation case study"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/phishing-investigation-case-study.git
git push -u origin main
```

If Git requests authentication, use GitHub's supported sign-in flow or Git Credential Manager; do not paste access tokens into chat.

**Never add the original EML, raw HTML/JS captures, or personal recipient information.**

Suggested GitHub description: `Defensive phishing investigation: email forensics, passive OSINT, static HTML comparison, and evidence-based attribution limits.`

Suggested topics: `cybersecurity`, `dfir`, `threat-intelligence`, `phishing-analysis`, `email-forensics`, `osint`, `python`.
