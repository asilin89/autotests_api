from clients.authentication.authentication_client import get_auth_client, AuthenticationClient
import pytest
from pydantic import BaseModel, EmailStr
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr: # access to email
        return self.request.email

    @property
    def password(self) -> str: # access to password
        return self.request.password


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture
def function_user(public_users_client) -> UserFixture: # function here highlights scope (i.e. @pytest.fixture(scope = function)
    request = CreateUserRequestSchema()                # if you need this to run at module scope = module_user
    response = public_users_client.create_user(request)     # done this way since fixture scope cannot be set dynamically
    return UserFixture(request=request ,response=response)