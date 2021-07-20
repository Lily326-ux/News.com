from requests import get

def make_get_request(url):
    request_result = get(url=url)
    print(request_result)
    if (request_result.status_code == 200):
        return request_result.json()
    else:
        raise Exception()

def return_get_string():
    return f'https://newsapi.org/v2/everything?q=tesla&from=2021-06-20&sortBy=publishedAt&apiKey=8836e4490fcf4387b55ae5bac665210b'