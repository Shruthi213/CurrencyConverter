from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "355c9a0ad99e4f6137ba"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()

    return data
def print_currencies(currencies):
    for currency in currencies:
        name = currency['CurrencyName']
        _id = currency['id']
        symbol = currency["CurrencySymbol"]
        print(f"{name}-{_id}-{symbol}")


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/currencies?apikey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)

    data = response.json()
    printer.pprint(data)

#data = get_currencies()
#print_currencies(data)
exchange_rate("USD","CAD")