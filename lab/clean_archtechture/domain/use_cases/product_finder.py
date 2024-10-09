from abc import ABC, abstractmethod


class ProductFinder(ABC):
    @abstractmethod
    def find(self, name) -> dict:
        pass
