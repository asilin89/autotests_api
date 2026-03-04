import pytest
from _pytest.fixtures import SubRequest
from pip._internal import operations
from sqlalchemy import lambda_stmt


@pytest.mark.parametrize("number", [1, -2, 3, 4, 5])
def test_numbers(number):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1,1),(2,4),(3,9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ["Windows", "Linux", "Mac OSX"])
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://qa.company.com",
    "https://prod.company.com"
])
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0


# How to parametrize a fixture: use params=
# request here != request in HTTP. it's pytest fixture request: keeps all data about fixture
@pytest.fixture(params=[
    "https://dev.company.com",
    "https://qa.company.com",
    "https://prod.company.com"
])
def host(request: SubRequest) -> str:
    return request.param # returns provided params - "https://dev.company.com etc


def test_host(host: str):
    print(f"Running test on host: {host}")


@pytest.mark.parametrize("user", ["Alica", "Laura"])
class TestOperations:
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self,user: str):
        print(f"User with no operations: {user}")



users = {
    "+37532999384": "User with money on bank account",
    "+14332343": "User with no money",
    "+48323428924": "User with operations on bank account"
}

# use ids= when need to add description to each param
@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids= lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    #print(f"Phone number: {phone_number}")
    pass