
import requests
import sys

def unmask():
    if len(sys.argv) < 2:
        sys.exit(1)
    else:
        # LEVEL 1: 4 spaces
        short_url = sys.argv[1]
        
        try:
            # LEVEL 2: 8 spaces
            response = requests.head(short_url, allow_redirects=False)
            
            if response.status_code in [301, 302]:
                # LEVEL 3: 12 spaces
                real_url = response.headers.get('Location')
                print(f"[+] Destination: {real_url}")
            else:
                # LEVEL 3: 12 spaces
                print("[-] No redirect")

        except requests.exceptions.RequestException as e:
            # LEVEL 2: 8 spaces (This MUST line up with the 'try')
            print(f"[!] Error: {e}")

if __name__=="__main__":
    unmask()
