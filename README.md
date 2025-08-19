
# OLEKC Tax Services – Website (Flask)

This is a lightweight, professional website for **OLEKC Tax Services**, built with **Flask**.  
It includes pages: Home, Services, About, Referral Program, Contact, and Pay Now.

## Quick Start
1) Create a virtual environment (optional)
2) Install requirements: `pip install -r requirements.txt`
3) (Optional) Set a payment link:
   - Windows PowerShell: `$env:OLEKC_PAYMENT_LINK="https://your-square-link"`
   - Mac/Linux: `export OLEKC_PAYMENT_LINK="https://your-square-link"`
4) Run: `python app.py`
Then open http://127.0.0.1:5000

## Customize
- Replace `static/img/logo-placeholder.png`
- Edit brand colors in `static/css/styles.css`
- Update pricing in `templates/services.html`
