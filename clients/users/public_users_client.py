from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.publich_http_builder import get_public_http_client


class User(TypedDict):

    """
    User structure description
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserRequestDict(TypedDict):

    """
    Structure description for create user request
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    user: User

class PublicUsersClient(APIClient):

    """
    Client to work with /api/v1/users endpoint.
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:

        """
        This function creates new user
        :param request: dict with email, password, lastName, firstName and middleName
        :return: httpx.Response object
        """

        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:

    """
    This function creates PublicUsersClient object with already configured http client.
    :return: ready to use PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())