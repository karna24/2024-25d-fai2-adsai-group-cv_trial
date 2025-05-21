import pytest
from PIL import Image
import io

from app.utils import validate_image  

@pytest.fixture
def valid_image_bytes():
    image = Image.new('RGB', (100, 100), color='blue')
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

@pytest.fixture
def corrupt_image_bytes():
    return b"This is not a valid image file"

def test_validate_image_with_valid_image(valid_image_bytes):
    assert validate_image(valid_image_bytes) is True

def test_validate_image_with_corrupt_data(corrupt_image_bytes):
    assert validate_image(corrupt_image_bytes) is False

def test_validate_image_with_empty_bytes():
    assert validate_image(b'') is False

def test_validate_image_with_partial_image():
    # Create a valid image and truncate it to simulate a corrupt image
    image = Image.new('RGB', (50, 50), color='red')
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='JPEG')
    partial_bytes = img_bytes.getvalue()[:10]  # Truncated image
    assert validate_image(partial_bytes) is False
