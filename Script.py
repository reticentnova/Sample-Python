import requests

R = requests.get("https://coreyms.com")
print(R.status_code)
