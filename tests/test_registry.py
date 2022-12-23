import pytest

from open_schema import SpecRegistry, SpecRoute


def fn(): pass


class TestSpecRegistry:

    def test_success(self, fake):
        name = fake.pystr()
        route = SpecRoute(name, doc=None, tag=None, request=None, responses=[])
        registry = SpecRegistry()
        registry.append(route, fn)

        assert registry[name] == (route, fn)
        assert list(registry) == [(route, fn)]

    def test_singletone(self, fake):
        name = fake.pystr()
        route = SpecRoute(name, doc=None, tag=None, request=None, responses=[])

        registry1 = SpecRegistry()
        registry2 = SpecRegistry()
        assert registry1 is registry2

        registry1.append(route, fn)
        assert registry1[name] == registry2[name]

    def test_fail_dublicate(self, fake):
        name = fake.pystr()

        registry = SpecRegistry()
        route1 = SpecRoute(name, doc=None, tag=None, request=None, responses=[])
        route2 = SpecRoute(name, doc=None, tag=None, request=None, responses=[])

        registry.append(route1, fn)
        with pytest.raises(KeyError):
            registry.append(route2, fn)
