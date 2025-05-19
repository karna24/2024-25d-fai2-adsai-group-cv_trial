import torch
from torchvision import transforms, models
from PIL import Image
import io
import torch.nn as nn

class ImageClassifier:
    def __init__(self, model_path):
        self.model = models.resnet18(pretrained=True)
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, 5)
        #self.model.fc = self.model.fc.cuda() if use_cuda else .fc
        #self.model = torch.load(model_path, map_location=torch.device('cpu'))
        checkpoint=torch.load(model_path, map_location=torch.device('cpu'))
        self.model.load_state_dict(checkpoint)
        self.model.eval()
    
        self.transform = transforms.Compose([
            transforms.Resize((150,150)),
            transforms.ToTensor(),  #0-255 to 0-1, numpy to tensors
            transforms.Normalize([0.5,0.5,0.5], # 0-1 to [-1,1] , formula (x-mean)/std
                [0.5,0.5,0.5])
        ])
        
        self.class_names = ['bargraph', 'flowchart', 'linegraph', 'piechart', 'scatterplot']  # Update with your class names

    def predict(self, image_bytes):
        image = Image.open(io.BytesIO(image_bytes))
        image = self.transform(image).unsqueeze(0)
        
        with torch.no_grad():
            outputs = self.model(image)
            _, predicted = torch.max(outputs, 1)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)[0]
            
        return {
            'class': self.class_names[predicted.item()],
            'confidence': probabilities[predicted.item()].item(),
            'all_probabilities': {
                cls_name: prob.item() for cls_name, prob in zip(self.class_names, probabilities)
            }
        }