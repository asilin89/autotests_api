from httpx import URL
from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict
from clients.private_http_builder import get_private_http_client, AuthUserDict


class User(TypedDict):

    """
    User structure description
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class GetUserResponseDict(TypedDict):
    user: User

class UpdateRequestDict(TypedDict):
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):

    """
    Client to work with /api/v1/users/
    """

    def get_user_me_api(self) -> Response:

        """
        Retrieves the current user's information
        :return: httpx.Response object
        """

        return self.get(url="/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:

        """
        Retrieves the user's information by its ID
        :param user_id: user's ID
        :return: httpx.Response object
        """

        return self.get(url=f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateRequestDict) -> Response:

        """
        Partially updates the user's information by its ID
        :param user_id: user's ID
        :param request: values which can be selected to be updated
        :return: httpx.Response object
        """

        return self.patch(url=f"/api/v1/users/{user_id}", json=request)
        ...

    def delete_user_api(self, user_id: str) -> Response:

        """
        Deletes the user's information by its ID
        :param user_id: user's ID
        :return: httpx.Response object
        """

        return self.delete(url=f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()

def get_private_users_client(user: AuthUserDict) -> PrivateUsersClient:

    """
    This function creates PrivateUsersClient object with configured HTTP client
    :param user:
    :return: Ready to use PrivateUsersClient object
    """
    return PrivateUsersClient(client=get_private_http_client(user))


