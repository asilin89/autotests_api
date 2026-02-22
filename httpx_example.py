import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)
# print(response.json())
#
# data = {
#     "title": "New Title ONe",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos/1", json=data)
#
# print(response.status_code)
# print(response.json())
#
# print("==========================================================")
#
# # Use data instead of json when sending application form params
#
# data = {
#     "username": "test_user_new",
#     "password": "zzoopp"
# }
#
# response = httpx.post("https://httpbin.org/post", data=data)
# # https://httpbin.org/post
#
# print(response.status_code)
# print(response.json())
# print("==========================================================")
#
# headers = {"Authorization": "Bearer test_token"}
#
# response = httpx.get("https://httpbin.org/get", headers=headers)
#
# print(response.status_code)
# print(response.request.headers)
# print(response.json())
# print("==========================================================")
#
# # Sending get request with params
#
# params = {"userId":1}
#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos/", params=params)
#
# print(response.status_code)
# print(response.json())

# print("==========================================================")
# # Working with files
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
#
# print(response.status_code)
# print(response.json())
# print("==========================================================")
#
# # Working with sessions
# # We use session when want to use it as an open connection for further requests
# # Client() in httpx is used to establish a constant connection with the server
#
# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(f"Response 1: {response1.json()}")
# print(f"Response 2: {response2.json()}")
# print("============================================================")
#
# # We create a client and providing auth token in headers
# # Then any new request will be using these headers. No need to provide it again
#
# client = httpx.Client(headers={"Authorization": "Bearer test_token"})
#
# response = client.get("https://httpbin.org/get")
# response3 = client.get("https://httpbin.org/get")
# response4 = client.get("https://httpbin.org/get")
#
# print(response.json())
# print(response3.json())
# print(response4.json())
#
# client.close()
print("=============================================================")

# Working with errors in httpx
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Request error: {e}")

# Case with timeout delay: we specify how much time we want request to be processed
# If timeout runs out - throwing error

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=5)
except httpx.ReadTimeout as e:
    print(f"Request timeout: {e}")


