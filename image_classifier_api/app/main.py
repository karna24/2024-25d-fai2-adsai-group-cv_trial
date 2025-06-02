from flask import Flask, request, jsonify
from .model import ImageClassifier
import os

app = Flask(__name__)

# Initialize model
model_path = os.getenv('MODEL_PATH', r'C:\Users\rewatkar.k\OneDrive - BUas\Desktop\2024-25d-fai2-adsai-group-cv_trial\image_classifier_api\app\best_checkpoint_resnet18.model')
classifier = ImageClassifier(model_path)


@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty file provided'}), 400
    
    try:
        image_bytes = file.read()
        prediction = classifier.predict(image_bytes)
        return jsonify(prediction)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)