import allure


# def test_feature():
#     with allure.step("Building API client"):
#         ...
#
#     with allure.step("Create course"):
#         ...
#
#     with allure.step("Delete course"):
#         ...

@allure.step("Building API client")
def build_api_client():
    with allure.step("Get user auth token"): # nested step under "Building API client"
        ...

    with allure.step("Create new API client"): # nested step under "Building API client"
        ...

@allure.step("Create course with title '{title}'") # step title with use actual value of title arg
def create_course(title: str):
    ...

@allure.step("Delete course")
def delete_course():
    ...

def test_feature():
    build_api_client()
    create_course()
    delete_course()