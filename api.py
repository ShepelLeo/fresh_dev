import requests
import logging
from jsonschema import validate
from schemas import ValidSchema

'''logger = logging.getLogger("__name__")'''


class SpookyUserAPI:
    def __init__(self, url):
        self.url = url

    def creation(self, data):
        path = "/api/users"
        response = requests.post(self.url + path, json=data)
        validate(instance=response.json(), schema=ValidSchema.CreateResponse)
        print(f"RESPONSE: {response.text}")
        return response
