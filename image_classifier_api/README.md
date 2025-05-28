Folder structure for sprint 1:
```
image_classifier_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   └── utils.py
├── tests/
├── pyproject.toml
└── README.md

```


## Docker 

Build docker image:

cd to image_classifier_api,

run : 
```
docker build -t image-classifier-api .

```



How to run the docker:

```

docker run -p 5000:5000 -v //app//best_checkpoint_resnet18.model://app//best_checkpoint_resnet18.model image-classifier-api

```
First path is the path to the local model folder, second path is to mount it to docker
