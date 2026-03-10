from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal
import allure


@allure.step("Assert create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Verifies that a user created successfully.
    :param request: request we send
    :param response: api response
    :raises AssertionError: if at lest 1 name doesn't match
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


@allure.step("Assert user")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Check that actual user data matches expected.
    :param actual: actual user data
    :param expected: expected user data
    :return:
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")


allure.step("Assert get user response")
def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
):
    """
    Verifies that a get user response matches create user response.
    :param get_user_response: get user API response
    :param create_user_response: create user API response
    :return:
    """
    assert_user(get_user_response.user, create_user_response.user)