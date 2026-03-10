from httpx import Request, RequestNotRead, Client

def make_curl_from_request(request: Request) -> str:
    """
    This function build a curl string from a request object.
    :param request: actual request object
    :return: curl string
    """
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    try:
        if body := request.content:
            result.append(f"-d '{body.decode("utf-8")}'")
    except RequestNotRead:
        pass

    return " \\\n ".join(result)


def print_request(request: Request):
    print(f"Running request: {request.method}")

client = Client(event_hooks={"request": [print_request]})
