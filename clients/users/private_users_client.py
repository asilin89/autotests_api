from httpx import URL
from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict
from clients.private_http_builder import get_private_http_client, AuthUserSchema
from clients.users.users_schema import UpdateRequestSchema, GetUserResponseSchema
import allure

from tools.routes import APIRoutes


class PrivateUsersClient(APIClient):

    """
    Client to work with /api/v1/users/
    """

    @allure.step("Get user me")
    def get_user_me_api(self) -> Response:

        """
        Retrieves the current user's information
        :return: httpx.Response object
        """

        #return self.get(url="/api/v1/users/me")
        return self.get(url=f"{APIRoutes.USERS}/me")

    @allure.step("Get user by id {user_id}")
    def get_user_api(self, user_id: str) -> Response:

        """
        Retrieves the user's information by its ID
        :param user_id: user's ID
        :return: httpx.Response object
        """

        #return self.get(url=f"/api/v1/users/{user_id}")
        return self.get(url=f"{APIRoutes.USERS}/{user_id}")

    @allure.step("Update user by id {user_id}")
    def update_user_api(self, user_id: str, request: UpdateRequestSchema) -> Response:

        """
        Partially updates the user's information by its ID
        :param user_id: user's ID
        :param request: values which can be selected to be updated
        :return: httpx.Response object
        """

        #return self.patch(url=f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))
        return self.patch(url=f"{APIRoutes.USERS}/{user_id}", json=request.model_dump(by_alias=True))
        ...

    @allure.step("Delete user by id {user_id}")
    def delete_user_api(self, user_id: str) -> Response:

        """
        Deletes the user's information by its ID
        :param user_id: user's ID
        :return: httpx.Response object
        """

        #return self.delete(url=f"/api/v1/users/{user_id}")
        return self.delete(url=f"{APIRoutes.USERS}/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

def get_private_users_client(user: AuthUserSchema) -> PrivateUsersClient:

    """
    This function creates PrivateUsersClient object with configured HTTP client
    :param user:
    :return: Ready to use PrivateUsersClient object
    """
    return PrivateUsersClient(client=get_private_http_client(user))


