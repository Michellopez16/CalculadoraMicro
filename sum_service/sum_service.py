from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Operation(BaseModel):
    a: float
    b: float

@app.post("/sum/")
def sum_numbers(operation: Operation):
    return {"result": operation.a + operation.b}