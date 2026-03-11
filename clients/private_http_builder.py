from httpx import Client
from typing import TypedDict
from pydantic import BaseModel, ConfigDict
from functools import lru_cache
from clients.authentication.authentication_client import get_auth_client
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.event_hooks import curl_event_hook
from config import settings


class AuthUserSchema(BaseModel):
    model_config = ConfigDict(frozen=True)
    email: str
    password: str

@lru_cache(maxsize=None)
def get_private_http_client(user: AuthUserSchema) -> Client:

    """
    This function creates httpx.Client obj with a user authentication
    :param user: AuthenticationUserSchema object with email and password
    :return: Ready to use httpx.Client object with user authentication
    """
    authentication_client = get_auth_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
        follow_redirects=True,
        event_hooks={"request": [curl_event_hook]}
    )
