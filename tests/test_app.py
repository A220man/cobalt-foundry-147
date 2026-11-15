from app.main import app
from fastapi.testclient import TestClient

def test_health():
    client = TestClient(app)
    resp = client.get('/api/health')
    assert resp.status_code == 200

