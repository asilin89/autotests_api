from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.publich_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):

    """
    Client to work with /api/v1/users endpoint.
    """
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:

        """
        This function creates new user
        :param request: dict with email, password, lastName, firstName and middleName
        :return: httpx.Response object
        """

        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request.model_dump(by_alias=True))
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:

    """
    This function creates PublicUsersClient object with already configured http client.
    :return: ready to use PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())