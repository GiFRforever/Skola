import urllib.request
import json

base_currency = "CZK"
target_currencies = ["EUR", "USD", "GBP"]

url = f"https://open.er-api.com/v6/latest/{base_currency}"
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())
print(data)
exchange_rates = data["rates"]

for currency, rate in exchange_rates.items():
    print(f"1 {base_currency} = {rate} {currency}")
