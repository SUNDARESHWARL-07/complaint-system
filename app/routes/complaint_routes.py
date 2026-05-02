from fastapi import APIRouter
from app.services.complaint_service import (
    create_complaint_service,
    get_complaints_service,
    get_complaints_by_status,
    get_complaints_with_defects,
    search_complaints   ,
    update_complaint_status,
get_complaints_paginated,
delete_complaint_service
)

router = APIRouter()


@router.post("/complaints")
def create_complaint(data: dict):
    return create_complaint_service(data)


@router.get("/complaints")
def get_complaints():
    return get_complaints_service()


@router.get("/complaints-with-defects")
def get_full_data():
    return get_complaints_with_defects()


@router.get("/complaints/filter")
def filter_complaints(status: str):
    return get_complaints_by_status(status)


@router.get("/complaints/search")
def search(query: str):
    return search_complaints(query)

@router.put("/complaints/{complaint_id}/status")
def update_status(complaint_id: int, status: str):
    return update_complaint_status(complaint_id, status)


@router.get("/complaints/paginated")
def get_paginated(skip: int = 0, limit: int = 10):
    return get_complaints_paginated(skip, limit)

@router.delete("/complaints/{complaint_id}")
def delete_complaint(complaint_id: int):
    return delete_complaint_service(complaint_id)