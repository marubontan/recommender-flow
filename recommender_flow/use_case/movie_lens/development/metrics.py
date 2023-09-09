from typing import List

from surprise import Prediction, accuracy

from recommender_flow.domain.metrics.mae import BaseMaeMetrics


class SurpriseMaeMetrics(BaseMaeMetrics):
    def __init__(self):
        pass

    def calculate(self, predictions: List[Prediction]) -> float:
        return accuracy.mae(predictions, verbose=False)
