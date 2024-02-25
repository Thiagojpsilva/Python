# Requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# HTTP --> 80, (Na web default)
# HTTPS --> 443 (Na web default)
url = 'http://localhost:8080/'

# GET --> leitura.
response = requests.get(url)
# print(response.content)
print(response.text)
