from pydantic import BaseModel, Field, HttpUrl
from tools.fakers import fake


class FileSchema(BaseModel):
    """
    File structure for file creation
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):

    """
    Request structure description for file creation
    """
    filename: str = Field(default_factory=lambda : f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """
    Response structure for file creation
    """
    file: FileSchema

class GetFileResponseSchema(BaseModel):
    file: FileSchema