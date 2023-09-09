from collections import defaultdict
from typing import Dict, List

from surprise import Prediction, accuracy

from recommender_flow.domain.metrics.base import BaseMetrics


class SurpriseMaeMetrics(BaseMetrics):
    def __init__(self):
        pass

    def calculate(self, predictions: List[Prediction]) -> float:
        return accuracy.mae(predictions, verbose=False)


class SurpriseHitRateMetrics(BaseMetrics):
    def __init__(self):
        pass

    def calculate(
        self,
        predictions: List[Prediction],
        predictions_with_action: List[Prediction],
        n: int = 10,
    ) -> float:
        top_n = self._get_top_n(predictions, n)
        hits = 0
        total = 0

        for prediction_with_action in predictions_with_action:
            for _, iid, _, _, _ in top_n[str(prediction_with_action.uid)]:
                if prediction_with_action.iid == iid:
                    hits += 1
                    break
            total += 1
        return hits / total

    def _get_top_n(
        self, predictions: List[Prediction], n: int
    ) -> Dict[int, List[Prediction]]:
        sorted_prediction = sorted(predictions, key=lambda x: (x.uid, -x.est))
        top_n = defaultdict(list)
        for prediction in sorted_prediction:
            if len(top_n[str(prediction.uid)]) < n:
                top_n[str(prediction.uid)].append(prediction)
        return top_n
