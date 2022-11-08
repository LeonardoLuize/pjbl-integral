from pydantic import BaseModel

class CalculatePayload(BaseModel):
    value_a: float
    value_b: float
    repeat_n: int

class ResponsePayload(BaseModel):
    value_a: float
    value_b: float
    repeat_n: int
    value: float