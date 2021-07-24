from helpers.helpers import make_get_request

class GetCurrency:
    def __init__(self, url):
        self.url = url

    def get_currency(self):
        try:
            return make_get_request(url=self.url)
        except:
            print('Check api, there are some error, on check your inernet connection')


data = GetCurrency('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
print(data.get_currency())