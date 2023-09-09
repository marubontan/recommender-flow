from dataclasses import dataclass
from typing import Dict, List, Optional
from uuid import UUID

from recommender_flow.domain.evaluator import Evaluation, ModelName
from recommender_flow.util.type.status import Status


@dataclass
class OutputDto:
    id: UUID
    status: Status
    message: Optional[str]
    evaluations: Optional[Dict[ModelName, List[Evaluation]]] = None
