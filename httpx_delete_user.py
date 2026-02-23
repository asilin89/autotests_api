import httpx
from tools.fakers import get_random_email


create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://127.0.0.1:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print("Create user data: ", create_user_response_data)

login_payload = {
    "email": create_user_response_data["user"]["email"],
    "password": "string"
}
login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response data: ", login_response_data)

# Deleting user

delete_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

delete_user_response = httpx.delete(
    f"http://127.0.0.1:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=delete_user_headers)

print("Delete user data: ", delete_user_response.status_code)
