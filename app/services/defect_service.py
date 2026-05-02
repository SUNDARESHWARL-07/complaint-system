from app.db.db import SessionLocal
from app.models.defect import Defect


def create_defect_service(data: dict):
    db = SessionLocal()
    try:
        defect = Defect(**data)
        db.add(defect)
        db.commit()
        return {"message": "Defect created"}
    finally:
        db.close()


def get_defects_service():
    db = SessionLocal()
    try:
        return db.query(Defect).all()
    finally:
        db.close()