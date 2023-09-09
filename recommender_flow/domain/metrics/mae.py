from abc import ABC, abstractmethod


class BaseMaeMetrics(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calculate(self, *args, **kwargs):
        pass
