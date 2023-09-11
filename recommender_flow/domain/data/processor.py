from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict

from recommender_flow.domain.data.layer import RawData, RefinedData, TrustedData


@dataclass
class ProcessedData:
    refined_data: RefinedData


# TODO: Docstring
class DataProcessManager(ABC):
    @abstractmethod
    def process(self) -> Dict[str, ProcessedData]:
        pass


class ToRaw(ABC):
    @abstractmethod
    def process(self) -> RawData:
        pass


class ToTrusted(ABC):
    @abstractmethod
    def process(self, *args, **kwargs) -> TrustedData:
        pass


class ToRefined(ABC):
    @abstractmethod
    def process(self) -> RefinedData:
        pass
