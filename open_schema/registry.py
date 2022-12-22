from dataclasses import dataclass

from typing import Callable, Dict, Iterable

from .models import SpecRoute


@dataclass
class SpecRegistryItem:

    spec: SpecRoute
    fn: Callable


class SpecRegistry:

    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    specs: Dict[str, SpecRegistryItem]

    def __init__(self):
        self.specs = {}

    def append(self, spec: SpecRoute, fn: Callable):
        name = spec.name
        if name in self.specs:
            raise KeyError(name)
        self.specs[name] = SpecRegistryItem(spec=spec, fn=fn)

    def __getitem__(self, name: str) -> SpecRegistryItem:
        return self.endpoints[name]

    def __iter__(self) -> Iterable[SpecRegistryItem]:
        return iter(self.specs.values())
