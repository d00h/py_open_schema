import json
from typing import Callable

from flask import Flask, request

from open_schema import SpecRegistry, SpecRoute

# from flask import request as http_request


def create_validate_func(spec: SpecRoute):
    def validator(**kwargs) -> dict:
        return kwargs
    return validator


def create_view_func(app: Flask, spec: SpecRoute, fn: Callable):
    ResponseClass = app.response_class
    validate = create_validate_func(spec)

    def wrapper(*args, **kwargs):
        status, data = fn(**validate(request))
        return ResponseClass(
            json.dumps(data), status=status, mimetype="application/json"
        )

    return wrapper


def register_routes(app: Flask):
    registry = SpecRegistry()
    for spec, fn in registry:  # type: SpecRoute
        print(spec.request.path)
        app.add_url_rule(
            spec.request.path,
            endpoint=spec.name,
            view_func=create_view_func(app, spec, fn),
            methods=spec.request.methods,
        )
