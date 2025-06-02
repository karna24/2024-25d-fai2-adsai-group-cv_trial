import requests

url = 'http://194.171.191.226:3215/predict'

with open(r'C:\Users\rewatkar.k\OneDrive - BUas\Desktop\ML_assigment_solution\ML_assigment_solution\Diagram_classifier_solution\dataset_split\dataset_split\test\bargraph\1702_2D00_multiserieschart.jpg', 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

print(response.json())