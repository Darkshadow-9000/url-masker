import requests
import sys

def unmask():
    if len(sys.argv) < 2:
        print("Usage: python unmask.py <short_url>")
        sys.exit(1)
    else:
        short_url = sys.argv[1]
        
        try:
            response = requests.head(short_url, allow_redirects=False, timeout=10)
            
            if 300 <= response.status_code < 400:
                real_url = response.headers.get('Location')
                if real_url:
                    print(f"[+] Destination: {real_url}")
                else:
                    print("[-] Redirect found but no Location header")
            else:
                print("[-] No redirect")

        except requests.exceptions.Timeout:
            print("[!] Error: Request timed out")
        except requests.exceptions.RequestException as e:
            print(f"[!] Error: {e}")

if __name__=="__main__":
    unmask()