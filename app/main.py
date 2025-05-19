from fastapi import FastAPI
from model import PyTorchModel
from schemas import PredictionInput, PredictionOutput
import os

app = FastAPI(title="PyTorch Model Server")

# Initialize model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/best_checkpoint_resnet18.model")
model = PyTorchModel(MODEL_PATH)

@app.get("/")
def read_root():
    return {"message": "PyTorch Model Serving API"}

@app.post("/predict", response_model=PredictionOutput)
async def predict(request: PredictionInput):
    """Make prediction with the PyTorch model"""
    try:
        result = model.predict(request.input_data)
        return result
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
def health_check():
    return {"status": "healthy", "device": model.device.type}