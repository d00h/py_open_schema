from typing import List

from .models import SpecRequest, SpecResponse, SpecRoute
from .registry import SpecRegistry


class SpecRouteBuilder:

    name: str
    tag: str
    doc: str = None
    request: SpecRequest = None
    responses: List[SpecResponse] = None

    def __init__(self, name: str):
        self.name = name

    def doc(self, text: str) -> 'SpecRouteBuilder':
        self.doc = text
        return self

    def tag(self, text: str) -> 'SpecRouteBuilder':
        self.tag = text
        return self

    def request(self, path: str, methods: list = None, body=None) -> 'SpecRouteBuilder':
        if self.request is not None:
            raise KeyError("dublicate 'request'")
        self.request = SpecRequest(
            path=path,
            methods=methods or ["GET"],
            body=body,
        )
        return self

    def response(
            self, status_code: int, model: type = None, mime_type: str = None,
            doc: str = None
    ) -> 'SpecRouteBuilder':
        if self.response is None:
            self.response = []
        response = SpecResponse(
            status_code=status_code,
            model=model,
            mime_type=mime_type or "application/json",
            doc=doc,
        )
        self.responses.append(response)
        return self

    def __call__(self, fn):
        registry = SpecRegistry()
        spec = SpecRoute(
            name=self.name, doc=self.doc, tag=self.tag,
            request=self.request, responses=self.request
        )
        registry.append(spec, fn)
