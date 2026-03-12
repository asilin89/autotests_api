from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
#from tcp_client import message
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
import allure
from config import settings
from tools.logger import get_logger

logger = get_logger("FILES_ASSERTIONS")


@allure.step("Assert create file response")
def assert_file_create_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Verifies that response matches request schema
    :param request: file create request schema
    :param response: API response with file details
    :raises AssertionError: if at least one field is missing or does not match
    """
    logger.info("Assert create file response")

    #expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename,"filename")
    assert_equal(response.file.directory, request.directory, "directory")


@allure.step("Assert file")
def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Verifies that response data matches actual schema
    :param actual: actual file data
    :param expected: expected file data
    :raises AssertionError: if at least one field is missing or does not match:
    """
    logger.info("Assert file")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")


@allure.step("Assert get file response")
def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
    Verifies that file get response matches actual create data
    :param get_file_response:
    :param create_file_response:
    :return:
    """
    logger.info("Assert get file response")
    assert_file(get_file_response.file, create_file_response.file)


@allure.step("Assert create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type = "string_too_short",
                input= "",
                context = {"min_length": 1},
                message = "String should have at least 1 character",
                location = ["body", "filename"]
            )
        ]
    )
    logger.info("Assert create file with empty filename response")
    assert_validation_error_response(actual, expected)


@allure.step("Assert create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type = "string_too_short",
                input= "",
                context = {"min_length": 1},
                message = "String should have at least 1 character",
                location = ["body", "directory"]
            )
        ]
    )
    logger.info("Assert create file with empty directory response")
    assert_validation_error_response(actual, expected)


@allure.step("Assert file not found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Check that correct error message is thrown if file not found
    :param actual: actual response
    :raises: AssertionError
    """
    logger.info("Assert file not found response")
    expected = InternalErrorResponseSchema(details= "File not found")
    assert_internal_error_response(actual, expected)


