import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
    
    def predict(self, data):
        """
            Predicts the output for the given input data using the trained model.

            Args:
                self: The instance of the ModelEvaluationPipeline class.
                data: The input data for prediction.

            Returns:
                The predicted output.

            Example:
                ```python
                pipeline = ModelEvaluationPipeline()
                input_data = ...
                prediction = pipeline.predict(input_data)
                print(prediction)
                ```
        """
        return self.model.predict(data)
