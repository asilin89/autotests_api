from pydantic import BaseModel, Field, ConfigDict
from typing import Any


class ValidationErrorSchema(BaseModel):
    """
    Model schema which describes a validation error
    """
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)

    type: str
    input: Any
    context: dict[str, Any] = Field(alias='ctx')
    message: str = Field(alias='msg')
    location: list[str] = Field(alias='loc')


class ValidationErrorResponseSchema(BaseModel):
    """
    Model schema which describes a response structure with error details
    """
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)

    details: list[ValidationErrorSchema] = Field(alias='detail')


class InternalErrorResponseSchema(BaseModel):
    """
    Model to describe internal error response
    """
    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias="detail")

