"""Importing modules"""
from fastapi.testclient import TestClient
from main import app
from mock import patch

client = TestClient(app=app)


@patch('openai.Image.create')
def test_generate_image(mock_openai):
    """Returns 200"""
    mock_openai.return_value = {
        "data": [{
            'url': 'generated-image-url'
        }]
    }

    response = client.post("/api/v1/image-generator",
                           json={'prompt': 'naturaleza'})
    assert response.status_code == 200
    assert response.json() == {'image': 'generated-image-url'}

# You need to create more test cases

# END
