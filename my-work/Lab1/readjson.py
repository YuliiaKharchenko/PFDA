# This program fetches the current Bitcoin price from the CoinDesk API,
# parses the JSON response, and prints the data



import requests

url ="https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)
data = response.json()
# print(data)
print(data['bpi']['EUR']['rate_float'])