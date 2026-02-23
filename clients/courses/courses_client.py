from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class GetCoursesQueryDict(TypedDict):

    """
    Request structure for getting all courses.
    """
    userId: str

class CreateCourseQueryDict(TypedDict):

    """
    Request structure for creating a course.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCourseRequestDict(TypedDict):

    """
    Request structure for updating a course.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(APIClient):

    """
    Client for getting all courses.
    """
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:

        """
        GET /api/v1/courses/
        :param query: course id
        :return: httpx.Response object
        """
        return self.get(f"/api/v1/courses/", params=query)

    def get_course_api(self, course_id: str) -> Response:

        """
        GET /api/v1/courses/{course_id}/
        :param course_id: query param
        :return: httpx.Response object
        """
        return self.get(f"/api/v1/courses/{course_id}/")

    def create_course_api(self, request: CreateCourseQueryDict) -> Response:

        """
        POST /api/v1/courses/ - create a course
        :param request: required params to create a course
        :return: httpx.Response object
        """
        return self.post(f"/api/v1/courses/", json=request)

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