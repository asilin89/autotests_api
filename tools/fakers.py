import time
from faker import Faker


class Fake:
    """
    This class is used to generate fake data using Faker library.
    """
    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        return self.faker.text()

    def uuid4(self) -> str:
        return self.faker.uuid4()

    def email(self) -> str:
        return self.faker.email()

    def sentence(self) -> str:
        return self.faker.sentence()

    def password(self) -> str:
        return self.faker.password()

    def last_name(self) -> str:
        return self.faker.last_name()

    def first_name(self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.middle_name()

    def estimated_time(self) -> str:
        return f"{self.integer_number(1,10)}"

    def integer_number(self, start: int =1, end: int = 100) -> int:
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        return self.faker.integer_number(50, 100)

    def min_score(self) -> int:
        return self.faker.integer_number(1, 49)

fake = Fake(faker=Faker())
#fake_ru = Faker(faker=Faker("ru_RU")) # All data will be generated in Russian
#fake_es = Faker(faker=Faker("es_ES")) # All data will be generated in Spanish

