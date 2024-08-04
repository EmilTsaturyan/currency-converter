# Currency Converter
This Python script allows you to convert currency using the CurrencyAPI. It prompts the user to input the base currency and the currencies to convert, and then displays the converted values.

## Prerequisites
[(https://skillicons.dev/icons?i=python)]
- Requests library (pip install requests)
- CurrencyAPI key (get it from CurrencyAPI)

## Setup
- Clone the repository:
```
git clone https://github.com/EmilTsaturyan/currency-converter.git
```
- Go to the clonned repository:
```
cd currency-converter
```
- Install dependencies:
```
pip install -r requirements.txt
```
- Create a config.py file and add your CurrencyAPI key:
```
API_KEY = 'your_currency_api_key'
```
- Run the script:
```
python currency_converter.py
```

## Usage

- Enter the base currency when prompted.
- Enter the currencies to convert (separated by commas) when prompted.
- View the converted values for each currency.


## Example 
```
Enter base currency: USD
Enter currencies (separated with ,): EUR,GBP,JPY
```
```
EUR - 0.85
GBP - 0.74
JPY - 103.02
```

