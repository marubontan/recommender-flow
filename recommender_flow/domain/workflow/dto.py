from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from recommender_flow.domain.evaluator import Evaluation


@dataclass
class WorkFlowDto:
    id: UUID
    created_at: datetime
    evaluation: Optional[Evaluation] =None
