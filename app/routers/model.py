from fastapi import APIRouter

router = APIRouter()


@router.get("/model/health")
def model_health():
    return {"status": "running"}