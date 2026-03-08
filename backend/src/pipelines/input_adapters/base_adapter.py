from abc import ABC, abstractmethod


class BaseInputAdapter(ABC):
    @abstractmethod
    def detect(self, source_path: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def extract_text(self, source_path: str) -> str:
        raise NotImplementedError
