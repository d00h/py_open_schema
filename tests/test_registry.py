import pytest

from open_schema import SpecRegistry


class TestSpecRegistry:

    def test_success(self):
        registry = SpecRegistry()

    def test_error(self):
        with pytest.raises(ValueError):
            raise ValueError()
