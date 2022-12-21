from requests import Request as HttpRequest
from requests import Response as HttpResponse

from open_schema import SchemaEndpoint, SchemaRegistry, SchemaRequest, SchemaResponse


class HttpClient:

    endpoint: Endpoift

    def __init__(self, endpoint: str):
        registry = Registry()
        self.endpint = registry[endpoint]

    def request(self, query, body) -> Response:
        request = HttpRequest(....)
        self.assert_request(self.endpoint.request, request)

        r = request.prepare()
        s = requests.Session()
        response = s.send(r)

        self.assert_request(self.endpoint.response, response)
        return response

    @staticmethod
    def assert_request(schema_request: SchemaRequest, http_request: HttpRequest):
        assert some
        some assertyion

    @staticmethod
    def assert_response(schema_responses: List[SchemaResponse], http_response: HttpResponse):
        for schema_response in schema_responses:
            assert some
            pass

        some assertyion
