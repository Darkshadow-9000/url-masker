
import requests
import sys

def unmask():
    if len(sys.argv) < 2:
        sys.exit(1)
    else:
        short_url = sys.argv[1]
        
        try:
            response = requests.head(short_url, allow_redirects=False)
            
            if response.status_code in [301, 302]:
                real_url = response.headers.get('Location')
                print(f"[+] Destination: {real_url}")
            else:
                print("[-] No redirect")

        except requests.exceptions.RequestException as e:
            print(f"[!] Error: {e}")

if __name__=="__main__":
    unmask()
