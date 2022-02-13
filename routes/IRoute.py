from abc import ABC, abstractmethod

class IRoute(ABC):

    @abstractmethod
    def get(self) -> dict:
        pass

