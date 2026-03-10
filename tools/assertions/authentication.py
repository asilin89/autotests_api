from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true
import allure


@allure.step("Assert login response")
def assert_login_response(response: LoginResponseSchema):
    """
    Verifies the valid response ig given after successful authorization.
    :param response: Response object with authorization token.
    :return:
    """
    assert_equal(response.token.token_type, "bearer", "token_type")
    assert_is_true(response.token.access_token, "access_token")
    assert_is_true(response.token.refresh_token, "refresh_token")