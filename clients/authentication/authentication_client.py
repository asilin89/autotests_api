from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict # we use TypeDict when want to specify exact key name in dict

from clients.publich_http_builder import get_public_http_client


class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginRequestDict(TypedDict):

    """
    Authentication Request Structure
    """

    email: str
    password: str

class LoginResponseDict(TypedDict):
    token: Token

class RefreshRequestDict(TypedDict):

    """
    Authentication Refresh Request Structure
    """

    refreshToken: str

class AuthenticationClient(APIClient):

    """
    Client for work with authentication (/api/v1/authentication/login)
    """

    def login_api(self, request: LoginRequestDict) -> Response:

        """
        This method does user authentication
        :param request: dict with email and password
        :return: httpx.Response object
        """

        return self.post(url="/api/v1/authentication/login",json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:

        """
        This method does token authentication refresh
        :param request: dict with refreshToken value
        :return: httpx.Response object
        """

        return self.post(url="/api/v1/authentication/refresh",json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)
        return response.json()

def get_auth_client() -> AuthenticationClient:

    """
    This function creates authentication client with configured httpx.Client
    :return: ready to use authentication client
    """
    return AuthenticationClient(client=get_public_http_client())