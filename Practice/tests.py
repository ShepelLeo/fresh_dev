from api import SpookyUserAPI
from models import SpookyUserGEN

URL = "https://reqres.in"


class TestAPI:
    @staticmethod
    def CommontestCreation():
        data = SpookyUserGEN().gen()
        response = SpookyUserAPI(URL).creation(data)
        assert response.status_code == 201


TestAPI().CommontestCreation()
