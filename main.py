from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import math
from typing import List
from pydantic import BaseModel
from app.solver import solve_quadratic

from database import models
from database.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class EquationResponse(BaseModel):
    coefficients: dict
    count: int
    roots: List[float]


@app.get("/solve", response_model=EquationResponse)
def solve_api(a: float, b: float, c: float,  db: Session = Depends(get_db)):
    roots = solve_quadratic(a, b, c)

    new_record = models.CalculationRecord(
        a=a, b=b, c=c, 
        roots=str(roots)
    )
    db.add(new_record)
    db.commit()

    return {
        "coefficients": {"a": a, "b": b, "c": c},
        "count": len(roots),
        "roots": roots
    }

