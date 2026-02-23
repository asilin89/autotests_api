from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict # we use TypeDict when want to specify exact key name in dict

class LoginRequestDict(TypedDict):

    """
    Authentication Request Structure
    """

    email: str
    password: str

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