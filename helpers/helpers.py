from requests import get

def make_get_request(url):
    request_result = get(url)
    if (request_result.status_code == 200):
        return request_result.json()
    else:
        raise Exception()

