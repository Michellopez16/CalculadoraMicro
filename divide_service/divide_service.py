from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

app = FastAPI()

class Operation(BaseModel):
    a: float
    b: float

@app.post("/divide/")
def divide_numbers(operation: Operation):
    if operation.b == 0:
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST, content={"message": "No se puede dividir por cero."})
    return {"result": operation.a / operation.b}
