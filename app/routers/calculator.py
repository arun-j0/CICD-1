from fastapi import APIRouter, HTTPException
from app.services.calculator_service import calculate_operation

router = APIRouter()

@router.get("/calculate")
def calculate(operation: str, num1: float, num2: float):
    try:
        result = calculate_operation(operation, num1, num2)
        return {"operation": operation, "num1": num1, "num2": num2, "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
