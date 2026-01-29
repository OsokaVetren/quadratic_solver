from sqlalchemy import Column, Integer, Float, String, DateTime, func
from database.database import Base

class CalculationRecord(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float)
    b = Column(Float)
    c = Column(Float)
    roots = Column(String) 
    created_at = Column(DateTime(timezone=True), server_default=func.now())