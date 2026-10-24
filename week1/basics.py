def format_usage(input_tokens: int, output_tokens: int) -> str:
    return f"in={input_tokens} out={output_tokens} total={input_tokens + output_tokens}"


def total_tokens(calls: list[dict]) -> dict:
    input_sum = sum(c["input"] for c in calls)
    output_sum = sum(c["output"] for c in calls)
    return {"input": input_sum, "output": output_sum, "total": input_sum + output_sum}
