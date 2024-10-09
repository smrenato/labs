from abc import ABC, abstractmethod


class ProductRegister(ABC):
    @abstractmethod
    def registry(self, http_request) -> dict:
        pass
