import torch
import numpy as np
from typing import Dict, Any

class PyTorchModel:
    def __init__(self, model_path: str):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.load_model(model_path)
        self.model.eval()
        self.class_names = ["class1", "class2", "class3", "class4", "class5"]  # Update with your classes

    def load_model(self, model_path: str) -> torch.nn.Module:
        """Load PyTorch model from file"""
        # Adjust based on how you saved your model
        model = torch.load(model_path, map_location=self.device)
        return model

    def preprocess(self, input_data: Any) -> torch.Tensor:
        """Convert input data to model-compatible tensor"""
        # Add your preprocessing logic here
        tensor = torch.tensor(input_data, dtype=torch.float32).to(self.device)
        return tensor

    def predict(self, input_data: Any) -> Dict[str, Any]:
        """Make prediction with the model"""
        with torch.no_grad():
            processed_input = self.preprocess(input_data)
            outputs = self.model(processed_input)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)
            confidence, predicted_class = torch.max(probabilities, 1)
            
        return {
            "predicted_class": self.class_names[predicted_class.item()],
            "confidence": confidence.item(),
            "class_probabilities": probabilities.cpu().numpy().tolist()[0]
        }