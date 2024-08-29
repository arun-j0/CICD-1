from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculator"}

@app.get("/calculate")
def calculate(operation: str, num1: float, num2: float):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation.")
    
    return {"operation": operation, "num1": num1, "num2": num2, "result": result}
