from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_create_user_response, assert_user
import allure
from tools.logger import get_logger

logger = get_logger("COURSES_ASSERTIONS")


@allure.step("Assert update course response")
def assert_update_course_response(
        request = UpdateCourseRequestSchema,
        response = UpdateCourseResponseSchema
):
    """
    Checks that the update course response contains an update course request.
    :param request: course update request
    :param response: API response with updated course data
    :return:
    """
    logger.info("Assert update course response")

    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")


@allure.step("Assert course")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    logger.info("Assert course")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)


@allure.step("Assert get courses response")
def assert_get_courses_response(
        get_courses_response = GetCoursesResponseSchema,
        create_course_responses = list[CreateCourseResponseSchema]
):
    """
    Verifies that get courses response matches create course response
    :param get_courses_response: API response with for list of courses request
    :param create_course_responses: list of API response with create course request
    :return:
    """
    logger.info("Assert get courses response")
    assert_length(get_courses_response.courses, create_course_responses, "courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_response.course)


@allure.step("Assert create courses response")
def assert_create_course_response(
        request = CreateCourseRequestSchema,
        response = CreateCourseResponseSchema
):
    """
    Verifies that create course response matches create course request
    :param request: create course request
    :param response: API response data
    :return:
    """
    logger.info("Assert create course response")
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")
    assert_equal(
        response.course.preview_file.id,
        request.preview_file_id,
        "preview_file_id"
    )
    assert_equal(
        response.course.created_by_user.id,
        request.created_by_user_id,
        "created_by_user_id"
    )



