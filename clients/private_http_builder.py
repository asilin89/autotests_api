from httpx import Client
from typing import TypedDict
from clients.authentication.authentication_client import get_auth_client, LoginRequestDict

class AuthUserDict(TypedDict):
    email: str
    password: str

def get_private_http_client(user: AuthUserDict) -> Client:

    """
    This function creates httpx.Client obj with a user authentication
    :param user: AuthenticationUserSchema object with email and password
    :return: Ready to use httpx.Client object with user authentication
    """
    authentication_client = get_auth_client()

    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://127.0.0.1:8000",
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )
