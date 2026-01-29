from fastapi.testclient import TestClient
from main import app
from app.solver import solve_quadratic
import pytest

client = TestClient(app)

def test_solver_two_roots():
    assert solve_quadratic(1, -3, 2) == [1.0, 2.0]

def test_solver_one_root():
    assert solve_quadratic(1, -2, 1) == [1.0]

def test_solver_no_roots():
    assert solve_quadratic(1, 0, 1) == []

def test_solver_linear():
    assert solve_quadratic(0, 2, -4) == [2.0]


def test_api_solve_endpoint():
    response = client.get("/solve?a=1&b=-3&c=2")
    
    assert response.status_code == 200
    
    data = response.json()
    assert data["count"] == 2
    assert data["roots"] == [1.0, 2.0]
    assert "coefficients" in data

def test_api_invalid_params():
    response = client.get("/solve?a=abc&b=0&c=1")
    assert response.status_code == 422 # Ошибка валидации Pydantic