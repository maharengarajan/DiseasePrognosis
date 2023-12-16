# End to End project of Disease Prognosis using MLOps techniques with MLFlow

# Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py

# To run this project

clone this repository
```
https://github.com/maharengarajan/DiseasePrognosis.git
```
create virtual environment
```
conda create -p venv python=3.8 -y
```
activate virtual environment
```
conda activate venv/
```
install requirements
```
pip install -r requirements.txt
```
finally run this command
```
python main.py
```

connect github repo with DagsHub and get mlflow tracking credentials
MLFLOW_TRACKING_URI=https://dagshub.com/maharengarajan/DiseasePrognosis.mlflow \
MLFLOW_TRACKING_USERNAME=maharengarajan \
MLFLOW_TRACKING_PASSWORD=d0af8cae7f0c8d195c580ac69666dfe9456157e1 \
python script.py


Run the below commands one by one in bash terminal to export as env variables:

```
export MLFLOW_TRACKING_URI=https://dagshub.com/maharengarajan/DiseasePrognosis.mlflow

export MLFLOW_TRACKING_USERNAME=maharengarajan 

export MLFLOW_TRACKING_PASSWORD=d0af8cae7f0c8d195c580ac69666dfe9456157e1
```

Finally run the blow command and see you trackings with mlflow
```
mlflow ui
```