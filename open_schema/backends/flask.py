from flask import Flask

from open_schema import SchemaRegistry


def register_endpoints(app: Flask):
    registry = SchemaRegistry()

    for endpoint in registry:
        app.add_url_rule(endpoint.request.path, ...)
