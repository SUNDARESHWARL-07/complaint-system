from fastapi import APIRouter
from app.services.defect_service import (
    create_defect_service,
    get_defects_service
)

router = APIRouter()

@router.post("/defects")
def create_defect(data: dict):
    return create_defect_service(data)


@router.get("/defects")
def get_defects():
    return get_defects_service()