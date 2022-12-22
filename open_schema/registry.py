from functools import lru_cache
from typing import Callable, Iterable, NamedTuple

from .models import SpecRoute


class SpecRegistryItem(NamedTuple):

    spec: SpecRoute
    fn: Callable


@lru_cache(maxsize=None)
class SpecRegistry:

    def __init__(self):
        self.specs = {}

    def append(self, spec: SpecRoute, fn: Callable):
        name = spec.name
        if name in self.specs:
            raise KeyError(name)
        self.specs[name] = SpecRegistryItem(spec=spec, fn=fn)

    def __getitem__(self, name: str) -> SpecRegistryItem:
        return self.specs[name]

    def __iter__(self) -> Iterable[SpecRegistryItem]:
        return iter(self.specs.values())
