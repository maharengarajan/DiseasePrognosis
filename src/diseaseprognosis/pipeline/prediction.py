import joblib
from pathlib import Path


# load the model & predict
class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))

    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction
