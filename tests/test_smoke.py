from pathlib import Path


def test_env_example_has_no_real_key():
    text = Path(".env.example").read_text()
    assert "sk-ant-" not in text
