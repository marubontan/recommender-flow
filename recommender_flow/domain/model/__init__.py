from abc import ABC
from datetime import datetime
from uuid import uuid4



class BaseModel(ABC):
    def __init__(self):
        self._id = uuid4()
        self._created_at = datetime.now()
