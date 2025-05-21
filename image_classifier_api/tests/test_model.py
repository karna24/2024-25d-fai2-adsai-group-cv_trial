import pytest
import torch
import io
from PIL import Image
from unittest.mock import patch, MagicMock
from app.model import ImageClassifier 

@pytest.fixture
def dummy_image_bytes():
    image = Image.new('RGB', (150, 150), color='white')
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

@pytest.fixture
def classifier(tmp_path):
    # Create a dummy model checkpoint and save it
    model = torch.hub.load('pytorch/vision', 'resnet18', pretrained=True)
    num_ftrs = model.fc.in_features
    model.fc = torch.nn.Linear(num_ftrs, 5)
    dummy_checkpoint_path = tmp_path / "dummy_model.pth"
    torch.save(model.state_dict(), dummy_checkpoint_path)
    
    return ImageClassifier(str(dummy_checkpoint_path))

def test_model_loads_correctly(classifier):
    assert isinstance(classifier.model, torch.nn.Module)
    assert classifier.model.fc.out_features == 5

def test_transform_applies_correctly(classifier, dummy_image_bytes):
    image = Image.open(io.BytesIO(dummy_image_bytes))
    transformed = classifier.transform(image)
    assert transformed.shape == (3, 150, 150)
    assert transformed.max().item() <= 1.0
    assert transformed.min().item() >= -1.0


def test_predict_returns_expected_format(classifier, dummy_image_bytes):
    mock_output = torch.tensor([[0.1, 0.2, 0.05, 0.15, 0.5]])

    with patch.object(classifier, 'model', return_value=mock_output):
        result = classifier.predict(dummy_image_bytes)

        assert 'class' in result
        assert 'confidence' in result
        assert 'all_probabilities' in result

def test_prediction_confidence_range(classifier, dummy_image_bytes):
    with patch.object(classifier, 'model') as mock_model:
        mock_model.return_value = torch.tensor([[0.2, 0.1, 0.3, 0.15, 0.25]])
        result = classifier.predict(dummy_image_bytes)
        assert 0.0 <= result['confidence'] <= 1.0
