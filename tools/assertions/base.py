from typing import Any, Sized
import allure
from tools.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")


@allure.step("Assert that response status code is equal {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Checks if the given response status code is equal to expected
    :param actual: status code from response
    :param expected: expected status code
    :return:
    """
    logger.info(f"Assert that response status code is equal to '{expected}'")
    assert actual == expected, f"Expected status code {expected}, but got status code {actual}"


@allure.step("Assert that {name} equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Checks if the given response is equal to expected
    :param actual: actual value
    :param expected: expected value
    :param name: asserted name (id, first_name, last_name etc.)
    :raises AssertionError: if actual != expected:
    """
    logger.info(f"Assert that '{name}' equals to '{expected}'")
    assert actual == expected, (
        f"Expected {name} to be {actual}, but got {expected}"
    )

@allure.step("Assert that {name} is true")
def assert_is_true(actual: Any, name: str):
    """
    Checks if the given response is true
    :param actual: actual value
    :param name: Validated object name
    :return:
    """
    logger.info(f"Assert that '{name}' is true")
    assert actual, (
        f"Incorrect value: {name}"
        f"Expected true value but got: {actual}"
    )


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Checks that length of the given response is equal to expected
    :param actual: actual value
    :param expected: expected value
    :param name: name of validated object
    :return:
    """
    with allure.step("Check that length of {name} equals to {len(expected)}"):
        logger.info(f"Assert that '{name}' length is equal to {len(expected)}")
        assert len(actual) == len(expected), f"Expected length: {expected}, but got length: {actual}"
