from typing import List, Optional, Type, Callable


class SchemaRequest:

    path: Optional[str]
    methods: List[str]

    body: Optional[Type]


class SchemaResponse:

    doc: Optional[str]
    status_code: int
    model: Optional[Type]


class SchemaEndpoint:

    name: str
    doc: Optional[str] = None

    request: SchemaRequest
    responses: List[SchemaResponse]
    fn: Callable

    def __init__(self, name: str):
        self.name = name
        self.request = SchemaRequest()
        self.responses = []

    def add_response(self, status_code: int, model: type, doc: str):
        response = SchemaResponse()
        response.status_code = status_code
        response.model = model
        response.doc = doc
        self.responses.append(response)
