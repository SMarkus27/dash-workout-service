from abc import ABC, abstractmethod


class IDivisionRepository(ABC):
    @classmethod
    @abstractmethod
    async def find(cls, name: str):
        pass

    @classmethod
    @abstractmethod
    async def create(cls, workout_type: dict):
        pass
