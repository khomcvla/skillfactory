import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def help():
        return  'Чтобы начать работу введите комманду боту в следующем формате:\n'\
                '<название или код валюты> '\
                '<в какую валюту конвертировать> '\
                '<количество конвертируемой валюты>\n'\
                'Просмотреть список доступных валют: /values'

    @staticmethod
    def values():
        text = 'Доступные валюты:'
        for key, value in keys.items():
            text = '\n'.join((text, f'- *{key}* ({value})'))
        return text

    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        if quote_ticker == base_ticker:
            raise ConvertionException(f'Невозможно конвертировать одинаковые валюты {quote}.')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote}')
        total_base = json.loads(r.content)['rates'][base] * int(amount)

        return total_base
