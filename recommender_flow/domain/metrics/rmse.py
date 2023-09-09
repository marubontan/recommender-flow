from abc import ABC, abstractmethod


class BaseRmseMetrics(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calculate(self, *args, **kwargs):
        pass
