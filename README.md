# 🔍 URL Unmasker
A lightweight, security-focused Python utility to safely reveal the destination of shortened URLs.

## 📖 Overview
In cybersecurity, attackers often use URL shorteners (Bitly, TinyURL, etc.) to hide malicious destinations or bypass email filters. This tool allows security researchers to "peek" behind the curtain without actually visiting the final destination in a browser.

## ✨ Features
* **Passive Reconnaissance:** Uses HTTP `HEAD` requests to fetch headers without downloading the body/payload.
* **Redirect Prevention:** Explicitly blocks automatic redirects to protect the host IP and avoid drive-by downloads.
* **CLI Integrated:** Designed to be used as a standard Linux utility via command-line arguments.
* **Error Handling:** Robust handling for connection timeouts and invalid URLs.

## 🚀 Usage
1. **Clone the repo:**
   ```bash
   git clone <your-repo-link>
   cd <repo-name>


2. Install dependencies:
   pip install requests


3. Run the tool:
   python3 unmask.py [https://bit.ly/example-link](https://bit.ly/example-link)



**Sample Output:

[*] Analyzing: [https://bit.ly/3xJkL](https://bit.ly/3xJkL)...
[+] Redirect Found!
[+] Destination: [https://malicious-site.com/payload.exe](https://malicious-site.com/payload.exe)
[+] Status Code: 301**
