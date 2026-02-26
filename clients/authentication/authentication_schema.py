from pydantic import BaseModel, Field
from tools.fakers import fake

class TokenSchema(BaseModel):
    """
    Authentication Token Schema Structure
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginRequestSchema(BaseModel):

    """
    Authentication Request Structure
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

class LoginResponseSchema(BaseModel):
    """
    Authentication Response Schema Structure
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):

    """
    Authentication Refresh Request Structure
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence())
