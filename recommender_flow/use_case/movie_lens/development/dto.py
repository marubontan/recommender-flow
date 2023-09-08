from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from recommender_flow.util.type.status import Status

@dataclass
class OutputDto:
    id: UUID
    status: Status
    message: Optional[str]