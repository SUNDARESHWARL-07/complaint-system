from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False)
    priority = Column(String(20), nullable=False)

    defects = relationship(
        "Defect",
        backref="complaint",
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<Complaint id={self.id} title={self.title}>"