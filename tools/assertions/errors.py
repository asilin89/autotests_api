from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
import allure
from tools.logger import get_logger

logger = get_logger("ERRORS_ASSERTIONS")


@allure.step("Assert validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Checks that the given validation error is equal to the expected one
    :param actual:
    :param expected:
    :return:
    """
    logger.info("Assert validation error")
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")


@allure.step("Assert validation error response")
def assert_validation_error_response(
        actual: ValidationErrorResponseSchema,
        expected: ValidationErrorResponseSchema
):
    """
    Checks that API response with validation error (ValidationErrorResponseSchema) matches expected one
    :param actual:
    :param expected:
    :return:
    """
    logger.info("Assert validation error response")
    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)


@allure.step("Assert internal error response")
def assert_internal_error_response(
        actual: InternalErrorResponseSchema,
        expected: InternalErrorResponseSchema
):
    """
    Checks internal error message (404 File not found)
    :param actual: Actual API response
    :param expected: Expected API response
    :raises: AssertionError
    """
    logger.info("Assert internal error response")
    assert_equal(actual.details, expected.details, "details")