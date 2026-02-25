from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict # we use TypeDict when want to specify exact key name in dict

from clients.publich_http_builder import get_public_http_client
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema


class AuthenticationClient(APIClient):

    """
    Client for work with authentication (/api/v1/authentication/login)
    """

    def login_api(self, request: LoginRequestSchema) -> Response:

        """
        This method does user authentication
        :param request: dict with email and password
        :return: httpx.Response object
        """

        return self.post(
            url="/api/v1/authentication/login",
            json=request.model_dump(by_alias=True))

    def refresh_api(self, request: RefreshRequestSchema) -> Response:

        """
        This method does token authentication refresh
        :param request: dict with refreshToken value
        :return: httpx.Response object
        """

        return self.post(
            url="/api/v1/authentication/refresh",
            json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        #return LoginResponseSchema(**response.json())
        return LoginResponseSchema.model_validate_json(response.text) # preferred method to use



def get_auth_client() -> AuthenticationClient:

    """
    This function creates authentication client with configured httpx.Client
    :return: ready to use authentication client
    """
    return AuthenticationClient(client=get_public_http_client())