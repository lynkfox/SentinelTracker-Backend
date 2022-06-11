import pytest
from common._snippets import *
from dataclasses import dataclass


class Test_Snippets:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_string_snippet_schema_generates(self):
        test_model = String(
            maxLength=5, minLength=1, format="date-time", pattern="(\\d{0})"
        )
        assert test_model.schema == {
            "type": "string",
            "minLength": 1,
            "maxLength": 5,
            "format": "date-time",
            "pattern": "(\\d{0})",
        }

    def test_string_snippet_schema_without_attributes_does_not_include_them(self):
        test_model = String()

        assert test_model.schema == {"type": "string"}

    def test_number_snippet_schema_generates(self):
        test_model = Number(min=5, max=10)
        assert test_model.schema == {"type": "number", "min": 5, "max": 10}

    def test_number_snippet_without_attributes_does_not_include_them(self):
        test_model = Number()
        assert test_model.schema == {"type": "number"}

    def test_integer_snippet_schema_generates(self):
        test_model = Integer(min=5, max=10)
        assert test_model.schema == {"type": "integer", "min": 5, "max": 10}

    def test_Integer_snippet_without_attributes_does_not_include_them(self):
        test_model = Integer()
        assert test_model.schema == {"type": "integer"}

    def test_array_snippet_schema_generates_with_simple_object_type(self):
        test_model = Array(items=[String])
        assert test_model.schema == {"type": "array", "items": ["string"]}

    def test_array_snippet_schema_generates_with_object_with_schema(self):
        @dataclass
        class Test:
            schema: dict

        test_model = Array(items=[Test(schema={"test": "test"})])
        assert test_model.schema == {"type": "array", "items": [{"test": "test"}]}
