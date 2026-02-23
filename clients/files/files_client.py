from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class CreateFileRequestDict(TypedDict):

    """
    Request structure description for file creation
    """
    filename: str
    directory: str
    upload_file: str

class FileClient(APIClient):

    """
    Client for /api/v1/files endpoint
    """
    def get_file_api(self, file_id: str) -> Response:

        """
        GET file api by id
        :param file_id:
        :return: httpx.Response object
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:

        """
        POST file api by id
        :param request: required parameters for file creation
        :return: httpx.Response object
        """
        return self.post(f"/api/v1/files",
                         data=request,
                         files={'upload_file': open(request['upload_file'], 'rb')})

    def delete_file_api(self, file_id: str) -> Response:

        """
        DELETE file api by id
        :param file_id:
        :return: httpx.Response object
        """
        return self.delete(f"/api/v1/files/{file_id}")