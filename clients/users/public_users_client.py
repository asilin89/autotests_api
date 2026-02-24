from clients.api_client import APIClient
from httpx import Response

from clients.publich_http_builder import get_public_http_client


class CreateUserRequestDict:
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        return self.post("/api/v1/users", json=request)

def get_public_users_client() -> PublicUsersClient:

    """
    This function creates PublicUsersClient object with already configured http client.
    :return: ready to use PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())