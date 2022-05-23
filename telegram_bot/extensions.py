import requests
import json
from config import keys


class ConvertionException(Exception):
    pass
class MoneyConverter:
    @staticmethod
    def convert( quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base} ')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать колличество {amount}')
        r = requests.get(f'https://v6.exchangerate-api.com/v6/2c7161729c4d19471144f5a8/pair/{quote_ticker}/{base_ticker}')
        total_base = json.loads(r.content)['conversion_rate']
        return round(total_base,2)*amount