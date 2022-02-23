
from abc import ABC, abstractmethod


class Cotroller(ABC):
    @abstractmethod
    def create_new(self, action):
        pass