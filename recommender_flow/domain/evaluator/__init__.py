from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List

from click import UUID

from recommender_flow.domain.data.processor import ProcessedData
from recommender_flow.domain.model import BaseModel

ModelName = str


@dataclass
class Evaluation:
    id: UUID
    model_id: UUID
    model_name: str
    metrics_name: str
    value: Any


class Evaluator(ABC):
    def __init__(self, models: List[BaseModel], *args, **kwargs):
        self._models = models

    @abstractmethod
    def execute(
        self, processed_data: ProcessedData
    ) -> Dict[ModelName, List[Evaluation]]:
        pass
