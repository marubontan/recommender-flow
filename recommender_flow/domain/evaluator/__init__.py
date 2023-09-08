from abc import ABC, abstractmethod
from dataclasses import dataclass
import datetime
from typing import List

from click import UUID

from recommender_flow.domain.model import BaseModel

@dataclass
class Evaluation:
    id: UUID
    model_id: UUID
    model_name: str
    metrics_name: str



class Evaluator(ABC):
    def __init__(self, models: List[BaseModel]):
        self._models = models
    
    @abstractmethod
    def execute(self, processed_data) -> List[Evaluation]:
        pass