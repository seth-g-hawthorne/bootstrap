# Adapted from: 

import os
import requests

# Enter your API key here
envvar_name = "OPENEXCHANGERATES_API_KEY"
api_key = os.getenv(envvar_name)
if not api_key:
    print(f"**** Error: Define {envvar_name} environment variable with your https://openexchangerates.org/ API key")
    exit()

# Set the API endpoint URL
url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

# Get the latest exchange rates from the API
response = requests.get(url)

# Parse the response JSON data
data = response.json()

# Get the base currency and exchange rates from the data
exchange_rates = data["rates"]

# Print the available currencies
available_currencies = ""

for currency in exchange_rates.keys():
    available_currencies += currency + ", "

# Remove the trailing comma and space
available_currencies = available_currencies[:-2]  

print("Available currencies: " + available_currencies)
    
# Get user input for the currency pair and amount to convert
from_currency = input("Enter the base currency: ").upper()
to_currency = input("Enter the target currency: ").upper()
amount = float(input("Enter the amount to convert: "))

# Calculate the converted amount
original_amount = amount / exchange_rates[from_currency]
converted_amount = original_amount * exchange_rates[to_currency]

# Print the result
print(f"{amount} {from_currency} = {converted_amount} {to_currency}")