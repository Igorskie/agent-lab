from dataclasses import dataclass

from pydantic import BaseModel, Field


@dataclass(frozen=True)
class Usage:
    input_tokens: int
    output_tokens: int

    @property
    def total(self) -> int:
        return self.input_tokens + self.output_tokens


class CallRecord(BaseModel):
    model: str
    input: int = Field(ge=0)
    output: int = Field(ge=0)


def total_usage(records: list[CallRecord]) -> Usage:
    input_sum = sum(r.input for r in records)
    output_sum = sum(r.output for r in records)
    return Usage(input_tokens=input_sum, output_tokens=output_sum)
