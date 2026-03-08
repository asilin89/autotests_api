from clients.courses.courses_client import CoursesClient, get_courses_client, CreateCourseRequestSchema, \
    CreateCourseResponseSchema
import pytest
from pydantic import BaseModel
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema # here must be schema
    response: CreateCourseResponseSchema # here must be schema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture,
) -> CourseFixture:
    request = CreateCourseRequestSchema(
        previewFileId=function_file.response.file.id,
        createdByUserId=function_user.response.user.id
    ) # here must be schema
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)

