import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
    
    

    def load_json(self):
        # pass
        raw = self.get_response_body()
        data = json.loads(raw)
        return data
    
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
information=get_requester.load_json()
print(information)