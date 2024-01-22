import requests
from config import API_KEY


def convert_currency(url:str, base_currency: str, currencies: str) -> dict:
    params = {
    'apikey': API_KEY,
    'currencies': currencies,
    'base_currency': base_currency
    }

    response = requests.get(url, params=params).json()
    return response

def print_info(info: dict) -> None:
    for data in info['data']:
        print(f'{data} - {round(info["data"][data]["value"], 2)}')

def main():
    url = "https://api.currencyapi.com/v3/latest?"

    base_currency = input('Enter bace currency: ').upper()
    currencies = input('Enter currencies (separated with ,): ').upper()

    info = convert_currency(url=url, base_currency=base_currency, currencies=currencies)
    print_info(info)

if __name__ == '__main__':
    main()