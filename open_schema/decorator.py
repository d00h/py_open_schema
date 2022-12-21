from .models import SchemaEndpoint
from .registry import SchemaRegistry


class SchemaEndpointBuilder:

    endpoint: SchemaEndpoint

    def __init__(self, endpoint):
        self.endpoint = SchemaEndpoint(endpoint)

    def doc(self, text: str) -> 'SchemaEndpointBuilder':
        self.endpoint.doc = text
        return self

    def path(self, path: str, methods: list = None) -> 'SchemaEndpointBuilder':
        self.endpoint.request.path = path
        self.endpoint.request.methods = methods or ['GET']
        return self

    def body(self, model: type) -> 'EndpointBuilder':
        self.endpoint.request.body = model
        return self

    def response(self, status_code: int, model: type = None, doc: str = None) -> 'SchemaEndpointBuilder':
        self.endpoint.add_response(status_code=status_code, model=model, doc=doc)
        return self

    def __call__(self, fn):
        print("register")
        registry = SchemaRegistry()
        self.endpoint.fn = fn
        registry.append(self.endpoint)
