from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, List, Union
from uuid import uuid4, UUID


class BaseData(ABC):
    @property
    @abstractmethod
    def content(self):
        pass

    @staticmethod
    def _generate_id() -> UUID:
        return uuid4()
    
    @staticmethod
    def _generate_created_at() -> datetime:
        return datetime.now()

class RawData(BaseData):
    def __init__(self, content: Any):
        self._id = self._generate_id()
        self._created_at = self._generate_created_at()
        self._content = content
    
    
    @property
    def content(self) -> Any:
        return self._content

class TrustedData(BaseData):
    def __init__(self, content: Any, raw_data_list: List[RawData]):
        self._id = self._generate_id()
        self._created_at = self._generate_created_at()
        self._content = content
        self._raw_data_list = raw_data_list
    
    @property
    def content(self) -> Any:
        return self._content

class RefinedData(BaseData):
    def __init__(self, content: Any, source_data_list: List[Union[TrustedData, 'RefinedData']]):
        self._id = self._generate_id()
        self._created_at = self._generate_created_at()
        self._content = content
        self._source_data_list = source_data_list
    
    @property
    def content(self) -> Any:
        return self._content