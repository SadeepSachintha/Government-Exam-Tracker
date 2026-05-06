import urllib.request
import re

try:
    js_content = urllib.request.urlopen('https://applications.doenets.lk/main-es2015.3cf48f023ca7d18580e2.js').read().decode('utf-8', errors='ignore')
    
    # Find all strings that look like API urls or paths
    # usually environment.apiUrl or similar
    urls = re.findall(r'(https?://[a-zA-Z0-9.-]+(?:/.*?api.*?|/.*?exam.*?))[\'"]', js_content)
    print("Found API URLs:")
    for u in set(urls):
        print(u)
        
    print("\n\nAll https strings containing doenets:")
    all_urls = re.findall(r'https?://[^\s"\'\\]*doenets[^\s"\'\\]*', js_content)
    for u in set(all_urls):
        print(u)
        
except Exception as e:
    print(e)
