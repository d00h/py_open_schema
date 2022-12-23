import inspect
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Tuple


class MapperKeyError(KeyError):
    pass


class MapperValueError(ValueError):
    pass


@dataclass
class Mapper:

    src_name: str
    dst_name: str
    annotation: Any

    @staticmethod
    def find_pairs(src: Dict[str, Any], dst: Dict[str, Any]) -> Iterable[Tuple[str, str]]:
        src_annotations = {
            annotation: name for name, annotation in src.items() if annotation is not None
        }
        for dst_name, dst_annotation in dst.items():
            if dst_name in src:
                src_name = dst_name
                yield (src_name, dst_name)
                continue

            if dst_annotation in src_annotations:
                src_name = src_annotations[dst_annotation]
                yield (src_name, dst_name)
                continue

            raise MapperKeyError(dst_name)

    @classmethod
    def create(cls, src: Dict[str, Any], dst: Dict[str, Any]) -> Iterable["Mapper"]:
        result = []
        for src_name, dst_name in cls.find_pairs(src, dst):
            src_annotation, dst_annotation = src[src_name], dst[dst_name]
            if src_annotation is not None and dst_annotation is not None and src_annotation != dst_annotation:
                raise MapperValueError(src_name, dst_name)

            mapper = cls(
                src_name=src_name,
                dst_name=dst_name,
                annotation=src_annotation or dst_annotation
            )
            result.append(mapper)
        if len(result) != len(src):
            diff = set(src.keys()) - set(m.src_name for m in result)
            raise MapperKeyError(*diff)

        if len(result) != len(dst):
            diff = set(dst.keys()) - set(m.dst_name for m in result)
            raise MapperKeyError(*diff)

        return result


def find_function_args(fn) -> Dict[str, Any]:
    def safe(p: inspect.Parameter):
        ParameterKind = inspect._ParameterKind
        if p.kind == ParameterKind.VAR_POSITIONAL:
            return p.name, list
        if p.kind == ParameterKind.VAR_KEYWORD:
            return p.name, dict
        if p.kind not in (ParameterKind.POSITIONAL_OR_KEYWORD, ParameterKind.POSITIONAL_ONLY):
            raise NotImplementedError(p.kind)

        if p.annotation is inspect._empty:
            return p.name, None

        return p.name, p.annotation

    args: inspect.Signature = inspect.signature(fn)

    return dict(safe(p) for p in args.parameters.values())
