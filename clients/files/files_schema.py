from pydantic import BaseModel, Field, HttpUrl

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
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """
    Response structure for file creation
    """
    file: FileSchema