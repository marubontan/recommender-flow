from typing import List

from surprise import SVD, Prediction, Trainset

from recommender_flow.domain.model.surprise import SurpriseBaseModel
from recommender_flow.domain.util.type import TestDataSchema


class SvdModel(SurpriseBaseModel):
    def __init__(self, name: str, random_state: int = 42):
        super().__init__(name)
        self._random_state = random_state
        self._model = SVD(random_state=random_state)

    def fit(self, data: Trainset):
        self._model.fit(data)

    def test(self, data: List[TestDataSchema]) -> List[Prediction]:
        return self._model.test(data)
