import requests

response = requests.get('https://boundary-information-dev.innovation-centre.com/v2/api-docs', timeout=10)

print(response)