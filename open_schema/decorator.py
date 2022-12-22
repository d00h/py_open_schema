
from .models import SpecRequest, SpecResponse, SpecRoute
from .registry import SpecRegistry


class SpecRouteBuilder:

    instance: SpecRoute

    def __init__(self, name: str):
        self.instance = SpecRoute(
            name=name, doc=None, tag=None,
            request=None, responses=[]
        )

    def doc(self, text: str) -> 'SpecRouteBuilder':
        self.instance.doc = text
        return self

    def tag(self, text: str) -> 'SpecRouteBuilder':
        self.instance.tag = text
        return self

    def request(self, path: str, methods: list = None, body=None) -> 'SpecRouteBuilder':
        if self.instance.request is not None:
            raise KeyError("dublicate request")
        self.instance.request = SpecRequest(
            path=path,
            methods=methods or ["GET"],
            body=body,
        )
        return self

    def response(
            self, status_code: int,
            doc: str = None, model: type = None, mime_type: str = None,
    ) -> 'SpecRouteBuilder':
        self.instance.responses.append(
            SpecResponse(
                status_code=status_code,
                model=model,
                mime_type=mime_type or "application/json",
                doc=doc,
            )
        )
        return self

    def __call__(self, fn):
        registry = SpecRegistry()
        registry.append(self.instance, fn)
