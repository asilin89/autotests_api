import httpx
from httpx import Client

from clients.event_hooks import curl_event_hook


def get_public_http_client() -> Client:

    """
    This function is used to create httpx.Client with base setup
    :return: ready to use httpx.Client
    """
    return Client(
        timeout=100,
        base_url="http://127.0.0.1:8000",
        #follow_redirects=True,
        event_hooks={"request": [curl_event_hook]}
    )
