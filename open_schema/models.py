from dataclasses import dataclass
from typing import Callable, List, Optional, Type


@dataclass
class SpecRequest:

    path: Optional[str]
    methods: List[str]

    body: Optional[Type]


@dataclass
class SpecResponse:

    status_code: int
    doc: Optional[str]

    mime_type: str
    model: Optional[Type]


@dataclass
class SpecRoute:

    name: str
    doc: Optional[str]
    tag: Optional[str]

    request: SpecRequest
    responses: List[SpecResponse]
