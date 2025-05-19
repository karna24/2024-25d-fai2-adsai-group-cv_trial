from pydantic import BaseModel
from typing import List

class PredictionInput(BaseModel):
    input_data: List[float]  # Update with your input shape
    
class PredictionOutput(BaseModel):
    predicted_class: str
    confidence: float
    class_probabilities: List[float]