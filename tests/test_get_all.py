import os
import sys

# Ensure the project root is importable so `src` can be found
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# Set environment variables before importing the app
os.environ["DATABASE_URL"] = "sqlite:///./test.db"
os.environ["MODEL_PATH"] = "data/model.pkl"

from fastapi.testclient import TestClient
from src.api import app
from src.database import engine
from src.models import Base

# Ensure the database is empty
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_get_all_preds_empty_returns_404():
    response = client.get("/getall")
    assert response.status_code == 404
    assert response.json() == {"detail": "No preds found in the database."}
