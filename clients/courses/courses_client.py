from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.courses.courses_schema import GetCourseQuerySchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from clients.files.files_client import FileClient
from clients.private_http_builder import get_private_http_client, AuthUserSchema
from clients.users.public_users_client import PublicUsersClient
from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


# class CourseSchema(BaseModel):
#     """
#     Course structure for getting a course.
#     """
#     id: str
#     title: str
#     maxScore: int
#     minScore: int
#     description: str
#     previewFile: FileSchema
#     estimatedTime: str
#     createdByUser: UserSchema
#
# class GetCoursesQuerySchema(BaseModel):
#
#     """
#     Request structure for getting all courses.
#     """
#     model_config = ConfigDict(populate_by_name=True)
#
#     user_id: str = Field(alias='userId')
#
# class CreateCourseRequestSchema(BaseModel):
#
#     """
#     Request structure for creating a course.
#     """
#
#     model_config = ConfigDict(populate_by_name=True)
#
#     title: str = Field(default_factory=fake.sentence)
#     maxScore: int = Field(alias='maxScore', default_factory=fake.max_score)
#     minScore: int = Field(alias='minScore', default_factory=fake.min_score)
#     description: str = Field(default_factory=fake.text)
#     estimatedTime: str = Field(alias='estimatedTime', default_factory=fake.estimated_time)
#     previewFileId: str = Field(alias='previewFileId', default_factory=fake.uuid4)
#     createdByUserId: str = Field(alias='createdByUserId', default_factory=fake.uuid4)
#
# class CreateCourseResponseSchema(BaseModel):
#     """
#     Response structure for creating a course.
#     """
#     course: CourseSchema
#
#
# class UpdateCourseRequestDict(TypedDict):
#
#     """
#     Request structure for updating a course.
#     """
#     title: str | None
#     maxScore: int | None
#     minScore: int | None
#     description: str | None
#     estimatedTime: str | None

class CoursesClient(APIClient):

    """
    Client for getting all courses.
    """
    def get_courses_api(self, query: GetCourseQuerySchema) -> Response:

        """
        GET /api/v1/courses/
        :param query: course id
        :return: httpx.Response object
        """
        return self.get(f"/api/v1/courses/", params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:

        """
        GET /api/v1/courses/{course_id}/
        :param course_id: query param
        :return: httpx.Response object
        """
        return self.get(f"/api/v1/courses/{course_id}/")

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:

        """
        POST /api/v1/courses/ - create a course
        :param request: required params to create a course
        :return: httpx.Response object
        """
        return self.post(f"/api/v1/courses/", json=request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request) -> Response:

        """
        PUT /api/v1/courses/{course_id}/- update a course
        :param course_id:
        :param request: required params to patch a course
        :return: httpx.Response object
        """
        return self.patch(f"/api/v1/courses/{course_id}/", json=request)

    def delete_course_api(self, course_id: str) -> Response:

        """
        DELETE /api/v1/courses/{course_id}/
        :param course_id:
        :return: httpx.Response object
        """
        response = self.delete(f"/api/v1/courses/{course_id}/")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

def get_courses_client(user: AuthUserSchema) -> CoursesClient:
    return CoursesClient(client=get_private_http_client(user))
