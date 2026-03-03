
from clients.authentication.authentication_client import get_auth_client, AuthenticationClient
import pytest
from pydantic import BaseModel, EmailStr
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema



@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_auth_client()
