from fastapi import APIRouter

from .controller import Controller
from .models import CalculatePayload, ResponsePayload

router = APIRouter(prefix="/api", tags=["Calculate"])
controller = Controller()


@router.post("/calculate", response_model=ResponsePayload)
async def calculate_integral(data: CalculatePayload):

    calculated_value = controller.calculate(data)

    return ResponsePayload(
        value_a=data.value_a,
        value_b=data.value_b,
        repeat_n=data.repeat_n,
        value=calculated_value,
    )