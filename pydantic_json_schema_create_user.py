from clients.authentication.authentication_schema import TokenSchema
from clients.private_http_builder import AuthUserSchema
from clients.users import public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
import jsonschema


# class TokenSchema(BaseModel):
#     """
#     Authentication Token Schema Structure
#     """
#     token_type: str = Field(alias="tokenType")
#     access_token: str = Field(alias="accessToken")
#     refresh_token: str = Field(alias="refreshToken")


print(TokenSchema.model_json_schema()) # Generates json schema from model


# Generated Schema
schema = {
    'description': 'Authentication Token Schema Structure',
    'properties': {
        'tokenType': {'title': 'Tokentype', 'type': 'string'},
        'accessToken': {'title': 'Accesstoken', 'type': 'string'},
        'refreshToken': {'title': 'Refreshtoken', 'type': 'string'}},
    'required': ['tokenType', 'accessToken', 'refreshToken'],
    'title': 'TokenSchema', 'type': 'object'}

####################################################################################


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email= fake.email(),
    password= "string",
    last_name= "string",
    first_name= "string",
    middle_name= "string"
)

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

# jsonschema.validate(instance=create_user_response.json(), schema=create_user_response_schema) default approach

################################## Negative Scenario #############################################

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_json = create_user_response.json()
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

del create_user_response_json['user']['email'] # Removing email field

validate_json_schema(instance=create_user_response_json, schema=create_user_response_schema)
#jsonschema.validate(instance=create_user_response_json, schema=create_user_response_schema)



