from httpx import Client, URL, QueryParams, Response
from typing import Any
from httpx._types import RequestData, RequestFiles


class APIClient:
    def __init__(self, client: Client):

        """
        Base API client which accepts httpx.Client instance
        :param client: instance of httpx.Client class to execute HTTP requests
        """

        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:

        """
        Executes HTTP GET request
        :param url: endpoint url
        :param params: get request params
        :return: Response object with response data
        """

        return self.client.get(url, params=params)

    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None) -> Response:

        """
        Executes HTTP POST request
        :param url: endpoint url
        :param json: data in request body (json)
        :param data: formatted data
        :param files: file data
        :return: response object with response data
        """

        return self.client.post(url, json=json, data=data, files=files)

    def patch(self, url : URL | str, json: Any | None = None) -> Response:
        return self.client.patch(url, json=json)

    def delete(self, url : URL | str) -> Response:
        return self.client.delete(url)
