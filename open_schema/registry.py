
from Typing import Dict, Iterable

from .models import SchemaEndpoint


class SchemaRegistry:

    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    endpoints: Dict[str, SchemaEndpoint]

    def __init__(self):
        self.endpoints = {}

    def append(self, endpoint: SchemaEndpoint):
        if endpoint.name in self.endpoints:
            raise KeyError(endpoint.name)
        self.endpoints[endpoint.name] = endpoint

    def __getitem__(self, name: str) -> SchemaEndpoint:
        return self.endpoints[name]

    def __iter__(self) -> Iterable[SchemaEndpoint]:
        return iter(self.endpoints.values())
