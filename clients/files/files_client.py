from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema

from clients.private_http_builder import get_private_http_client, AuthUserSchema
import allure
from clients.api_coverage import tracker
from tools.routes import APIRoutes


class FileClient(APIClient):

    """
    Client for /api/v1/files endpoint
    """
    @allure.step("Get file by file id {file_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.FILES}/{{file_id}}")
    def get_file_api(self, file_id: str) -> Response:

        """
        GET file api by id
        :param file_id:
        :return: httpx.Response object
        """
        #return self.get(f"/api/v1/files/{file_id}")
        return self.get(f"{APIRoutes.FILES}/{file_id}")

    @allure.step("Create file")
    @tracker.track_coverage_httpx(APIRoutes.FILES)
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:

        """
        POST file api by id
        :param request: required parameters for file creation
        :return: httpx.Response object
        """
        # return self.post(f"/api/v1/files",
        #                  data=request.model_dump(by_alias=True, exclude={'upload_file'}), # excludes upload_file field from request
        #                  files={'upload_file': open(request.upload_file, 'rb')})
        return self.post(f"{APIRoutes.FILES}",
                         data=request.model_dump(by_alias=True, exclude={'upload_file'}),
                         # excludes upload_file field from request
                         files={'upload_file': open(request.upload_file, 'rb')})


    @allure.step("Delete file by id {file_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.FILES}/{{file_id}}")
    def delete_file_api(self, file_id: str) -> Response:

        """
        DELETE file api by id
        :param file_id:
        :return: httpx.Response object
        """
        #return self.delete(f"/api/v1/files/{file_id}")
        return self.delete(f"{APIRoutes.FILES}/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)

def get_files_client(user: AuthUserSchema) -> FileClient:

    """
    This function creates FilesClient object with configured http client
    :param user:
    :return: Ready to use FilesClient object
    """
    return FileClient(client=get_private_http_client(user))