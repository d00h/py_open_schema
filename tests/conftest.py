import pytest
from faker import Faker
from faker.providers import BaseProvider


class CustomProvider(BaseProvider):

    def pytype(self) -> type:
        return type(f"Type_{self.random_int()}", (), {})


@pytest.fixture(scope="session")
def fake():
    faker = Faker()
    faker.add_provider(CustomProvider)
    yield faker
