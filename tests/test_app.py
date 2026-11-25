from app.main import app, validate_shots
from fastapi.testclient import TestClient

def test_health():
    client = TestClient(app)
    resp = client.get('/api/health')
    assert resp.status_code == 200

def test_shots_schema():
    """Validate that all SHOTS entries conform to the expected schema.
    
    This regression test ensures shot data consistency for the Remotion
    video skill pipeline. It verifies that every shot entry has the
    required fields (id, title, duration, transition, theme) with
    correct types.
    """
    validate_shots()
