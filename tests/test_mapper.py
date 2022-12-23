import pytest

from open_schema.mapper import (
    Mapper, MapperKeyError, MapperValueError, find_function_args
)


class TestMapperFindPairs:

    def test_success_by_name(self, fake):
        src_name = fake.pystr()
        src = {src_name: None}
        dst = {src_name: None}
        pairs = Mapper.find_pairs(src, dst)

        assert list(pairs) == [(src_name, src_name)]

    def test_success_by_annotation(self, fake):
        src_name, dst_name = fake.pystr(), fake.pystr()
        annotation = fake.pytype()

        src = {src_name: annotation}
        dst = {dst_name: annotation}
        pairs = Mapper.find_pairs(src, dst)

        assert list(pairs) == [(src_name, dst_name)]

    def test_fail(self, fake):
        src = {fake.pystr(): fake.pystr()}
        dst = {fake.pystr(): fake.pystr()}

        with pytest.raises(MapperKeyError):
            for old_name, new_name in Mapper.find_pairs(src, dst):
                pass


class TestMapperCreate:

    def test_success_by_name(self, fake):
        src_name = fake.pystr()
        annotation = fake.pytype()
        src = {src_name: annotation}
        dst = {src_name: None}

        result = Mapper.create(src, dst)

        assert result == [
            Mapper(src_name=src_name, dst_name=src_name, annotation=annotation)
        ]

    def test_success_by_annotation(self, fake):
        src_name, dst_name = fake.pystr(), fake.pystr()
        annotation = fake.pytype()
        src = {src_name: annotation}
        dst = {dst_name: annotation}

        result = Mapper.create(src, dst)

        assert result == [
            Mapper(src_name=src_name, dst_name=dst_name, annotation=annotation)
        ]

    def test_fail_by_different_name(self, fake):
        src = {fake.pystr(): None}
        dst = {fake.pystr(): None}

        with pytest.raises(MapperKeyError):
            Mapper.create(src, dst)

    def test_fail_by_different_annotation(self, fake):
        name = fake.pystr()
        src_annotation, dst_annotation = fake.pytype(), fake.pytype()

        src = {name: src_annotation}
        dst = {name: dst_annotation}

        with pytest.raises(MapperValueError):
            Mapper.create(src, dst)

    def test_fail_src_bigger(self, fake):
        name, lost_name = fake.pystr(),  fake.pystr()
        src = {name: None, lost_name: None}
        dst = {name: None}

        with pytest.raises(MapperKeyError) as exinfo:
            Mapper.create(src, dst)

        ex: MapperKeyError = exinfo.value
        assert ex.args == (lost_name,)

    def test_fail_dst_bigger(self, fake):
        name, lost_name = fake.pystr(),  fake.pystr()
        src = {name: None}
        dst = {name: None, lost_name: None}

        with pytest.raises(MapperKeyError) as exinfo:
            Mapper.create(src, dst)

        ex: MapperKeyError = exinfo.value
        assert ex.args == (lost_name,)


class TestFindFunctionArgs:

    @staticmethod
    def fn1(name: str, size: int, some):
        pass

    def test_fn1(self):
        assert find_function_args(self.fn1) == {
            "name": str,
            "size": int,
            "some": None,
        }

    @staticmethod
    def fn2(hello=1, *args, **kwargs):
        pass

    def test_fn2(self):
        assert find_function_args(self.fn2) == {
            "hello": None,
            "args": list,
            "kwargs": dict,
        }
