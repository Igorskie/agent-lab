from week1.basics import format_usage, total_tokens


def test_format_usage():
    assert format_usage(22, 77) == "in=22 out=77 total=99"


def test_total_tokens_sums_all_calls():
    calls = [
        {"model": "haiku", "input": 22, "output": 77},
        {"model": "haiku", "input": 10, "output": 5},
    ]
    assert total_tokens(calls) == {"input": 32, "output": 82, "total": 114}


def test_total_tokens_empty_list():
    assert total_tokens([]) == {"input": 0, "output": 0, "total": 0}
