from fastapi import FastAPI, Request
import httpx

app = FastAPI()

# Direcciones de los microservicios
#SERVICES = {
#    "sum": "http://sum-service:8001",
#    "subtract": "http://subtract-service:8002",
#    "multiply": "http://multiply-service:8003",
#    "divide": "http://divide-service:8004"
#}
SERVICES = {
    "sum": "http://localhost:8001",
    "subtract": "http://localhost:8002",
    "multiply": "http://localhost:8003",
    "divide": "http://localhost:8004"
}


@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def gateway(service: str, path: str, request: Request):
    if service not in SERVICES:
        return {"error": "Servicio no encontrado"}

    service_url = SERVICES[service]
    method = request.method
    client = httpx.AsyncClient()

    try:
        # Redirigir la solicitud al servicio correspondiente
        async with client.stream(method, f"{service_url}/{path}", content=await request.body()) as response:
            return await response.json()
    finally:
        await client.aclose()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)