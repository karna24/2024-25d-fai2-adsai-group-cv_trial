import logging
from PIL import Image
import io

def validate_image(image_bytes):
    """Validate that the uploaded file is an image"""
    try:
        img = Image.open(io.BytesIO(image_bytes))
        img.verify()
        return True
    except Exception:
        return False