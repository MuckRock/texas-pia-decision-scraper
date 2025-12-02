import random
import time

import requests


def scrape_texas_ag_decisions():
    base_url = "https://www2.texasattorneygeneral.gov/opinions/openrecords/PIA/51paxton/orl/2025/pdf/or2025{:06d}.pdf"
    
    for i in range(0, 50000):  
        url = base_url.format(i)
        print(f"Trying: {url}")
        
        try:
            response = requests.get(url, timeout=10)
            print(f"Status code: {response.status_code}")
            
            if response.status_code == 200:
                filename = f"docs/or2025{i:06d}.pdf"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {filename}")
            elif response.status_code == 404:
                print(f"Not found: or2025{i:06d}")
            else:
                print(f"Error {response.status_code} for: or2025{i:06d}")
                
        except requests.RequestException as e:
            print(f"Request failed for or2025{i:06d}: {e}")
        
        time.sleep(random.uniform(1, 2))

scrape_texas_ag_decisions()