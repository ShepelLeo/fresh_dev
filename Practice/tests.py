from api import SpookyUserAPI
from models import SpookyUserGEN

URL = "https://reqres.in"


class TestAPI:
    def test_api(self):
        data = SpookyUserGEN().gen()
        response = SpookyUserAPI(URL).creation(data)
        assert response.status_code == 201
