from open_schema import SchemaRegistry


def get_controller(name: str):
    registry = SchemaRegistry()
    return registry[name]
