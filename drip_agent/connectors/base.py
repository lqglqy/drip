from abc import ABC, abstractmethod


class BaseConnector(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def list(self, path: str):
        pass
