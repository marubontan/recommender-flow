from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional

from recommender_flow.domain.data.layer import RawData, RefinedData, TrustedData


@dataclass
class Dataset:
    name: str
    refined_data_list: List[RefinedData]

    @property
    def list(self) -> List[str]:
        return [refined_data.name for refined_data in self.refined_data_list]

    def get(self, name: str) -> Optional[RefinedData]:
        return next(
            (
                refined_data
                for refined_data in self.refined_data_list
                if refined_data.name == name
            ),
            None,
        )


# TODO: Docstring
class DataProcessManager(ABC):
    def get(self, name: str) -> Optional[Dataset]:
        return next(
            (dataset for dataset in self._datasets if dataset.name == name), None
        )

    @abstractmethod
    def process(self):
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
