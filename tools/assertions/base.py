from typing import Any

def assert_status_code(actual: int, expected: int):
    """
    Checks if the given response status code is equal to expected
    :param actual: status code from response
    :param expected: expected status code
    :return:
    """
    assert actual == expected, f"Expected status code {expected}, but got status code {actual}"

def assert_equal(actual: Any, expected: Any, name: str):
    """
    Checks if the given response is equal to expected
    :param actual: actual value
    :param expected: expected value
    :param name: asserted name (id, first_name, last_name etc.)
    :raises AssertionError: if actual != expected:
    """
    assert actual == expected, (
        f"Expected {name} to be {actual}, but got {expected}"
    )