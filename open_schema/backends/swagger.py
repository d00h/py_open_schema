from open_schema import SpecRegistry



def generate_swagger() -> dict:
    registry = SchemaRegistry()
    return {
       "swagger": "2.0",
       "routes": [
          generate_swagger_endpoint(endpoint.spec) for endpoint in registry
       ]
    }


def generate_swagger_endpoint(endpoint: SchemaEndpoint) -> dict:
    return {}

