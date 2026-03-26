from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.services.system_services import (
    get_health_info,
    get_cpu_info,
    get_memory_info,
    get_all_metrics,
    get_current_time
)

router = APIRouter(prefix="/api/v1", tags=["Monitoring"])

def build_error_response(message: str, status_code: int = 500):
    return JSONResponse(
        status_code = status_code,
        content={
            "error": message,
            "status": status_code,
            "checket_at": get_current_time()
        }
    )

@router.get("/health")
def health():
    try:
        return JSONResponse(status_code=200, content=get_health_info())
    except Exception as e:
        return build_error_response(str(e), 500)

@router.get("/memory")
def health():
    try:
        return JSONResponse(status_code=200, content=get_memory_info())
    except Exception as e:
        return build_error_response(str(e), 500)


@router.get("/all")
def all_metrics():
    try:
        return JSONResponse(status_code=200, content=get_all_metrics())
    except Exception as e:
        return build_error_response(str(e), 500)