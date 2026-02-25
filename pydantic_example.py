from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str = "Gomel"
    zip_code: str = "9410"

class User(BaseModel):
    id: int
    name: str
    email: str
    #address: Address
    is_active: bool = Field(alias="isActive")

user = User(
    id=10,
    name="Alex",
    email="aaa@text.com",
    #address=Address() - will take default values from Address
    #address={"city": "Dobrush", "zip_code": "1122"}
    #address=Address(city="Minsk", zip_code="1190")
    isActive=True
)

print(user)
print(user.email)

print(user.model_dump()) # converts model data to dict

print(user.model_dump_json()) # converts model data to json

#################### Alias Example ######################################

user_data = {
    "id": 1,
    "name": "Alex",
    "email": "alex@test.com",
    "isActive": True
}

user1 = User(**user_data) # extracts user_data dict
print("user1: ", user1.model_dump())
