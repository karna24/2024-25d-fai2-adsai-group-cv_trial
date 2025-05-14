[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/i4PR14xw)


Folder structure for Sprint 1:

pytorch-model-deployment/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── model.py         # PyTorch model wrapper
│   └── schemas.py       # Pydantic models
├── models/
│   └── model_weights.pth  # Your trained model
├── tests/               # Unit tests
├── pyproject.toml       # Poetry config
├── Dockerfile
└── README.md