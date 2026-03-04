import pytest

#@pytest.fixture(autouse=True, scope='module')
@pytest.fixture(autouse=True) # autouse=True means this fixture will be applied to each test automatically
def send_analytics_data():
    print("[AUTOUSE] Sending analytics data...")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Initializing autotests settings")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Creating a user data once per class")

@pytest.fixture(scope="function") # function is used as default setting
def user_client(settings): # nested fixture
    print("[FUNCTIONS] Creating an API client per each autotest")


class TestUserFlow:
    def test_user_can_login(self, settings, user, user_client):
        ...

    def test_can_create_course(self, settings, user, user_client):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, user_client):
        ...

@pytest.fixture
def user_data():
    print("[SETUP] Creating a user data before test run") # running BEFORE test
    yield {"username": "test_user", "email": "test@example.com"} # the fixture itself -> data can be used in TEST
    print("[TEARDOWN] Deleting a user data after test ran") # running AFTER test


def test_user_email(user_data: dict):
    print(user_data)
    assert user_data["email"] == "test@example.com"


def test_user_username(user_data: dict):
    print(user_data)
    assert user_data["username"] == "test_user"
