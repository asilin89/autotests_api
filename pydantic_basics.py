
"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""

import uuid
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel

# Field - used for aliases
# ConfigDict - used when need to set alias cases by default
# computed_field - used when need to add a field to schema
# HttpUrl - to validate http str format
# EmailStr - to validate email str format

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str

    @computed_field
    def username(self) -> str:
        return f"{self.firstName} {self.lastName}"

    def get_username(self) -> str:
        return f"{self.firstName} {self.lastName}"


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True) # automatically converts snake_case to camelCase

    id: str = Field(default_factory=lambda: str(uuid.uuid4)) # generates random str by default
    title: str
    max_score: int = Field(alias="maxScore")
    #max_score: int
    min_score: int = Field(alias="minScore")
    #min_score: int
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    #estimated_time: str
    created_by_user: UserSchema = Field(alias="createdByUser")

course_default_model = CourseSchema(
    id="course-id",
    title="Course Title",
    maxScore=100,
    minScore=10,
    description="Course description",
    previewFile=FileSchema(
        id="preview-file-id",
        filename="preview-file-name.png",
        directory="courses",
        url="https://example.com/"
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="user-id",
        email="agd@test.com",
        lastName="Last",
        firstName="First",
        middleName="Middle",
    )
)

print("Course default model: ", course_default_model)
print(type(course_default_model))
############################## Model initializing through dict ##############################

course_dict = {
    "id": "course-id",
    "title": "Course Title",
    "maxScore": 100,
    "minScore": 10,
    "description": "Course description",
    "previewFile": {
        "id": "preview-file-id",
        "filename": "preview-file-name.png",
        "directory": "courses",
        "url": "https://example.com/"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "agd@test.com",
        "lastName": "Last",
        "firstName": "First",
        "middleName": "Middle"
    }
}

# Creating a model based on course_dict dict
course_dict_model = CourseSchema(**course_dict) # de-serialization (dict -> model)

print("Course dict model: ", course_dict_model)
print(type(course_dict_model))

############################## Model initializing through JSON ##############################

course_json = """
{  
    "id": "course-id",
    "title": "Course Title",
    "maxScore": 100,
    "minScore": 10,
    "description": "Course description",
    "previewFile": {
        "id": "preview-file-id",
        "filename": "preview-file-name.png",
        "directory": "courses",
        "url": "https://example.com/"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "agd@test.com",
        "lastName": "Last",
        "firstName": "First",
        "middleName": "Middle"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json) # de-serialization (json -> model)
print("Course json model: ", course_json_model)

############################## Serialization (Model -> json/dict) ##############################

c_dict = course_json_model.model_dump(by_alias=True) # Model -> dict
print(c_dict)
c_json = course_json_model.model_dump_json(by_alias=True) # Model -> json
print(c_json)

############################## Example with Model method get_username ##############################
user = UserSchema(
        id="user-id",
        email="agd@test.com",
        lastName="Last",
        firstName="First",
        middleName="Middle"
)

print(user.get_username())
print(user.get_username(), user.username) # create new field in model "username" and assigns value to it

############################## Handling invalid format data ##############################

try:
    file = FileSchema(
        id="preview-file-id",
        filename="preview-file-name.png",
        directory="courses",
        url="localhost"
    )
except ValidationError as e:
    print(e)
    print(e.errors)