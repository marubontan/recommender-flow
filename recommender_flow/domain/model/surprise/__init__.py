from abc import ABC, abstractmethod
from typing import List

from surprise import Trainset
from surprise.prediction_algorithms.predictions import Prediction

from recommender_flow.domain.model import BaseModel
from recommender_flow.domain.util.type import TestDataSchema


class SurpriseBaseModel(BaseModel, ABC):
    def __init__(self, name: str):
        super().__init__(name)

    @abstractmethod
    def fit(self, data: Trainset):
        pass

    @abstractmethod
    def test(self, data: List[TestDataSchema]) -> List[Prediction]:
        pass
