import pytest


@pytest.mark.smoke
def test_smoke_case():
    assert 1 + 1 == 2


@pytest.mark.regression
def test_regression_case():
    assert 2 * 2 == 4

@pytest.mark.fast
def test_fast():
    ...

@pytest.mark.slow
def test_slow():
    ...

@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        ...

    def test_case2(self):
        ...

@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self): # equals to @pytest.mark.regression @pytest.mark.smoke
        ...

    @pytest.mark.slow
    def test_password_reset(self): # equals to @pytest.mark.regression @pytest.mark.slow
        ...

    def test_logout(self):
        ...

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    ...

@pytest.mark.api
class TestUserInterface:
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login(self):
        ...

    @pytest.mark.regression
    def test_forgot_password(self):
        ...

    @pytest.mark.smoke
    def test_signup(self):
        ...