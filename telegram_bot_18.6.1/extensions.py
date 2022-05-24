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
            raise ConvertionException(f'Не удалось обработать валюту {quote}.\nПодсказка - /help,\nВалюты - /values')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.\nПодсказка - /help,\nВалюты - /values')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать колличество {amount}')
        r = requests.get(f'https://v6.exchangerate-api.com/v6/2c7161729c4d19471144f5a8/pair/{quote_ticker}/{base_ticker}')
        # Your API Key: 2c7161729c4d19471144f5a8
        # Example Request: https://v6.exchangerate-api.com/v6/2c7161729c4d19471144f5a8/pair/USD/EUR


        total_base = json.loads(r.content)['conversion_rate']
        return round(total_base,2)*amount