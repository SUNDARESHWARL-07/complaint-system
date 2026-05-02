from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Defect(Base):
    __tablename__ = "defects"

    id = Column(Integer, primary_key=True, index=True)
    complaint_id = Column(Integer, ForeignKey("complaints.id"))
    description = Column(String(255))
    status = Column(String(50))