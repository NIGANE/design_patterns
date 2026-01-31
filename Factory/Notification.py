from abc import ABC, abstractmethod
from typing import Any


class Notification(ABC):

    @abstractmethod
    def send(s, message: str = None) -> Any:
        pass
