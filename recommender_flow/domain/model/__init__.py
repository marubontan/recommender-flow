from abc import ABC
from datetime import datetime
from uuid import UUID, uuid4


class BaseModel(ABC):
    def __init__(self, name):
        self._id = uuid4()
        self._name = name
        self._created_at = datetime.now()

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name
