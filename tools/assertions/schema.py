from typing import Any
from jsonschema import validate, FormatChecker
from jsonschema.validators import Draft202012Validator

def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Validates actual response (JSON obj) and its schema
    :param instance: actual response
    :param schema: expected schema
    :raises jsonschema.exceptions.ValidationError: if validation fails
    :return: None
    """
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )