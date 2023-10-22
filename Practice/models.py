from faker import Faker

fake = Faker()


class SpookyUserGEN:
    @staticmethod
    def gen():
        username = fake.name()
        userjob = fake.job()
        return {"name": username, "job": userjob}
