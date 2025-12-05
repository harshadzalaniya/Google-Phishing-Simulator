# Google Phishing Simulator (Educational Purpose Only)

A realistic Google login page clone built with **Flask** for authorized **security awareness training**, **red team engagements**, and **ethical phishing simulations**.

**This tool is strictly for legal and authorized use only** (e.g., company security training, CTF challenges, penetration testing with explicit permission).

### Features
- 99% visually identical to real Google login
- Floating labels & "Show password" functionality
- Silently captures credentials + IP + User-Agent
- Instantly redirects to real `accounts.google.com` (victim suspects nothing)
- Clean logging to `captured/credentials.txt`
- Mobile responsive

### Preview
![Screenshot](screenshot.png)  
*(Add your own screenshot later)*

### Folder Structure
It Will be same as the repository.
Google-Phishing-Simulator/
├── app.py
├── captured/                  ← Credentials saved here
├── templates/index.html
└── static/
├── css/style.css
└── images/logo.png


### Installation & Usage
```bash
# 1. Clone repo
git clone https://github.com/yourusername/Google-Phishing-Simulator.git
cd Google-Phishing-Simulator

# 2. Install Flask
pip install flask

# 3. Run locally
python app.py



