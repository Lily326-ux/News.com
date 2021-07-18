from helpers.helpers import make_get_request

class Get_News:
    def __init__(self, url):
        self.url = url


    def get_all_news(self):
        try:
            return make_get_request(url=self.url)
        except:
            print('Check api, there are some error, on check your inernet connection')


'''
---USAGE OF THIS CLASS

this class get url as argument and set it to self

 1) Method get_all_news make request to our api with url we have, and return us Dict with arrays and another dicts
 
 *** Practical Usage ***
 
 return_get_string() -> return string, url
 
 data = Get_News(return_get_string())
 print(data.get_all_news())
 
 you can find documentation and response from get request HERE https://newsapi.org/
'''