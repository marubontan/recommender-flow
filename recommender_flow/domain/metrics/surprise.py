from typing import List

from surprise import Prediction, accuracy

from recommender_flow.domain.metrics.base import BaseMetrics


class SurpriseMaeMetrics(BaseMetrics):
    def __init__(self):
        pass

    def calculate(self, predictions: List[Prediction]) -> float:
        return accuracy.mae(predictions, verbose=False)
