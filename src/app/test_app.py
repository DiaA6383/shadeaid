import os
import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_image(client):
    # Path to a sample image file
    image_path = 'src/tests/sample_image.png'
    with open(image_path, 'rb') as img:
        data = {
            'file': (img, 'sample_image.png')
        }
        response = client.post('/', content_type='multipart/form-data', data=data)
        assert response.status_code == 200
        assert 'Grayscale Image' in response.get_data(as_text=True)
        assert 'Shading Image' in response.get_data(as_text=True)