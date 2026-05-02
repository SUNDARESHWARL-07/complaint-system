from app.db.db import SessionLocal
from app.models.complaint import Complaint
from sqlalchemy.orm import joinedload

def create_complaint_service(data: dict):
    db = SessionLocal()
    try:
        priority = get_priority(data["title"])   

        complaint = Complaint(
            title=data["title"],
            status=data["status"],
            priority=priority
        )

        db.add(complaint)
        db.commit()
        db.refresh(complaint)

        return {
            "message": "Complaint created",
            "priority": priority
        }
    finally:
        db.close()


def get_complaints_service():
    db = SessionLocal()
    try:
        return db.query(Complaint).all()
    finally:
        db.close()

def get_complaints_with_defects():
    db = SessionLocal()
    try:
        complaints = db.query(Complaint).options(
            joinedload(Complaint.defects)
        ).all()

        result = []
        for c in complaints:
            result.append({
                "id": c.id,
                "title": c.title,
                "status": c.status,
                "defects": [
                    {
                        "id": d.id,
                        "description": d.description,
                        "status": d.status
                    } for d in c.defects
                ]
            })

        return result
    finally:
        db.close()

def get_complaints_by_status(status: str):
    db = SessionLocal()
    try:
        return db.query(Complaint).filter(Complaint.status == status).all()
    finally:
        db.close()
def search_complaints(query: str):
    db = SessionLocal()
    try:
        return db.query(Complaint).filter(
            Complaint.title.ilike(f"%{query}%")
        ).all()
    finally:
        db.close()

def get_priority(title: str):
    title = title.lower()

    if "crash" in title or "failure" in title:
        return "HIGH"
    elif "slow" in title or "delay" in title:
        return "MEDIUM"
    else:
        return "LOW"
VALID_FLOW = {
    "OPEN": ["IN_PROGRESS"],
    "IN_PROGRESS": ["RESOLVED"],
    "RESOLVED": ["CLOSED"],
    "CLOSED": []
}


def update_complaint_status(complaint_id: int, new_status: str):
    db = SessionLocal()
    try:
        complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()

        if not complaint:
            return {"error": "Complaint not found"}

        if new_status not in VALID_FLOW.get(complaint.status, []):
            return {"error": f"Invalid transition from {complaint.status} to {new_status}"}

        complaint.status = new_status
        db.commit()

        return {"message": "Status updated", "new_status": new_status}
    finally:
        db.close()
def get_complaints_paginated(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    try:
        return db.query(Complaint).offset(skip).limit(limit).all()
    finally:
        db.close()
def delete_complaint_service(complaint_id: int):
    db = SessionLocal()
    try:
        complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()

        if not complaint:
            return {"error": "Complaint not found"}

        db.delete(complaint)
        db.commit()

        return {"message": "Deleted successfully"}
    finally:
        db.close()