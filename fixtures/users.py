from clients.authentication.authentication_client import get_auth_client, AuthenticationClient
import pytest
from pydantic import BaseModel, EmailStr

from clients.private_http_builder import AuthUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
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

    @property
    def authentication_user(self) -> AuthUserSchema:
        return AuthUserSchema(email=self.email, password=self.password)

@pytest.fixture()
def authentication_client() -> AuthenticationClient:
    return get_auth_client()

@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture()
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture: # function here highlights scope (i.e. @pytest.fixture(scope = function)
    request = CreateUserRequestSchema()                # if you need this to run at module scope = module_user
    response = public_users_client.create_user(request)     # done this way since fixture scope cannot be set dynamically
    return UserFixture(request=request ,response=response)