import pytest
from pydantic import ValidationError

from week1.models import CallRecord, Usage, total_usage


def test_usage_total_property():
    u = Usage(input_tokens=22, output_tokens=77)
    assert u.total == 99


def test_usage_is_frozen():
    u = Usage(input_tokens=1, output_tokens=2)
    with pytest.raises(AttributeError):
        u.input_tokens = 5


def test_call_record_from_dict():
    r = CallRecord.model_validate({"model": "haiku", "input": 22, "output": 77})
    assert r.model == "haiku"
    assert r.input == 22


def test_call_record_converts_numeric_string():
    r = CallRecord.model_validate({"model": "haiku", "input": "22", "output": 77})
    assert r.input == 22


def test_call_record_rejects_negative_tokens():
    with pytest.raises(ValidationError):
        CallRecord.model_validate({"model": "haiku", "input": -5, "output": 77})


def test_call_record_rejects_missing_field():
    with pytest.raises(ValidationError):
        CallRecord.model_validate({"model": "haiku", "input": 22})


def test_total_usage_from_records():
    records = [
        CallRecord(model="haiku", input=22, output=77),
        CallRecord(model="haiku", input=10, output=5),
    ]
    assert total_usage(records) == Usage(input_tokens=32, output_tokens=82)
