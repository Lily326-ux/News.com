from requests import get

from constants.constants import news_api_key

def make_get_request(url):
    request_result = get(url=url)
    if (request_result.status_code == 200):
        return request_result.json()
    else:
        raise Exception()

def return_get_string():
    return f'https://newsapi.org/v2/everything?q=tesla&from=2021-06-19&sortBy=publishedAt&apiKey={news_api_key}'