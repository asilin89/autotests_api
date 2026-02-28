from pydantic import BaseModel, Field, ConfigDict, EmailStr
from tools.fakers import fake

class UserSchema(BaseModel):

    """
    User structure description
    """
    model_config = ConfigDict(populate_by_name=True)  # allows to use fields in snake_case when initialize schema obj

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):

    """
    Structure description for create user request
    """
    model_config = ConfigDict(populate_by_name=True) # allows to use fields in snake_case when initialize schema obj

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.first_name)

class CreateUserResponseSchema(BaseModel):
    user: UserSchema

class UpdateRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)  # allows to use fields in snake_case when initialize schema obj

    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)

class UpdateUserResponseSchema(BaseModel):
    """
    Structure description for update user response
    """
    user: UserSchema

class GetUserResponseSchema(BaseModel):
    """
    Structure description for get user response
    """
    user: UserSchema