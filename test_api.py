import urllib.request

url = 'https://doenets.lk/examcalendar'
headers = {
    'User-Agent': 'Mozilla/5.0'
}

try:
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    data = res.read().decode('utf-8', errors='ignore')
    print("SUCCESS", res.getcode())
    print("Response Length:", len(data))
    if 'api' in data.lower() or 'json' in data.lower() or '[' in data[:50]:
        print(data[:500])
except Exception as e:
    print("Error:", e)
