from open_schema import SpecRegistry, SpecRoute


def generate_swagger() -> dict:
    registry = SpecRegistry()
    return {
        "swagger": "2.0",
        "routes": [
            generate_swagger_endpoint(endpoint.spec) for endpoint in registry
        ]
    }


def generate_swagger_endpoint(endpoint: SpecRoute) -> dict:
    return {}
