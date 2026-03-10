from httpx import Request
import allure
from tools.http.curl import make_curl_from_request


def curl_event_hook(request: Request):
    """
    This function builds a curl string from a request object and attaches it to allure report.
    :param request:
    :return:
    """
    curl_command = make_curl_from_request(request)

    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)
