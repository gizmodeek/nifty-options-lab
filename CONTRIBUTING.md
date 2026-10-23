# Contributing to Options Learning Lab

Thank you for helping! This project teaches options math. It is for learning only.

## Ground rules
- No broker logins, API keys, account numbers, or real personal trade records. Ever.
- No trading advice or "best trade" rankings. Explanations and calculators only.
- Keep the warnings. Every risk-related change should say what can go wrong.

## Step by step (new to GitHub?)
1. Create a free GitHub account at github.com.
2. Click **Fork** (top right of the repo page). This makes your own copy.
3. Clone your copy: `git clone https://github.com/YOUR-NAME/nifty-options-lab.git`
4. Make a branch: `git checkout -b my-improvement`
5. Make your change. Test it:
   - Open `web/index.html` in your browser.
   - Run `python -m pytest tests -q` (install with `python -m pip install pytest`).
6. Save and send:
   ```
   git add .
   git commit -m "Short description of the change"
   git push -u origin my-improvement
   ```
7. On GitHub, click **Compare & pull request**, describe what you changed and why, and submit.

## What we welcome
- Fixes to explanations (clearer wording, correct terms)
- Tests for the math
- Accessibility and phone-layout fixes
- Better tooltips and glossary entries

## Review
The maintainer reviews every pull request before it is merged. Be patient and kind.
