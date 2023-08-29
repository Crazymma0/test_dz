import requests

url = "https://s.amazon-adsystem.com/ecm3?ex=yieldmoHMT&id=EcpS3VvZTtWnOKVQ3KPCaw"

payload = {}
headers = {
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)