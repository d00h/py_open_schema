from flask import Flask, jsonify
from flask import request as http_request

from open_schema import SchemaEndpoint, SchemaRegistry


def create_view_func(app: Flask, endpoint: SchemaEndpoint):
    def wrapper():
        schema_request = endpoint.request
        body = http_request.json
        return app.response_class(f"{dumps(data, indent=indent, separators=separators)}\n",

    return wrapper

def register_endpoints(app: Flask):
    registry=SchemaRegistry()

    for endpoint in registry:  # type: SchemaEndpoint
        app.add_url_rule(
            endpoint.request.path,
            endpoint=endpoint.name,
            view_func=create_view_func(endpoint)
        )
