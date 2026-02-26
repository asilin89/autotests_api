from api_client_get_user import authentication_user
from clients.courses.courses_client import CoursesClient, get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client
from clients.private_http_builder import AuthUserSchema
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from tools.fakers import fake
from clients.users.users_schema import CreateUserRequestSchema
from clients.files.files_schema import CreateFileRequestSchema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename='new_image.png',
    directory='courses',
    upload_file='./testdata/files/altlayer.png'
)

create_file_response = files_client.create_file(create_file_request)

print("Create file data: ", create_file_response)

create_course_request = CreateCourseRequestDict(
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)

create_course_response = courses_client.create_course(create_course_request)
print("Create course data: ", create_course_response)