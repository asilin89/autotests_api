from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema
from tools.assertions.base import assert_equal


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