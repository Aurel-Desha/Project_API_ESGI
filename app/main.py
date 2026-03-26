from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routes.monitoring import router
from app.services.system_services import get_current_time

app = FastAPI(title="Monitoring API", version="1.0.0")

app.include_router(router)

@app.exception_handler(404)
def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Endpoint not found",
            "status": 404,
            "checked_at": get_current_time()
        }
    )