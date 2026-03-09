from http import HTTPStatus

import pytest

from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FileClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from fixtures.files import FileFixture
from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_file_create_response, assert_get_file_response, \
    assert_create_file_with_empty_filename_response, assert_create_file_with_empty_directory_response, \
    assert_file_not_found_response
from tools.assertions.schema import validate_json_schema
import allure
from allure_commons.types import Severity


@pytest.mark.files
@pytest.mark.regression
@allure.tag(AllureTag.FILES, AllureTag.REGRESSION)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeature.FILES)
class TestFiles:
    @allure.title("Create File")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_create_file(self, files_client: FileClient):
        request = CreateFileRequestSchema(upload_file="./testdata/files/altlayer.png")
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_file_create_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.title("Get File")
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_get_file(self, files_client: FileClient, function_file: FileFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)

        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.title("Create File with Empty Filename")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_create_file_with_empty_filename(self, files_client: FileClient):
        request = CreateFileRequestSchema(
            filename="",
            upload_file="./testdata/files/altlayer.png"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Create File with Empty Directory")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_create_file_with_empty_directory(self, files_client: FileClient):
        request = CreateFileRequestSchema(
            filename="",
            upload_file="./testdata/files/altlayer.png"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.title("Delete File")
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_delete_file(self, files_client: FileClient, function_file: FileFixture):
        delete_response = files_client.delete_file_api(function_file.response.file.id)

        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = files_client.get_file_api(function_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_file_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.title("Get File with Invalid File Id")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_get_file_with_incorrect_file_id(self, files_client: FileClient):
        response = files_client.get_file_api("invalid-file-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        #assert_get_file_with_incorrect_file_id_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

