from abc import ABC, abstractmethod


class IExercisesRepository(ABC):
    @classmethod
    @abstractmethod
    async def find(cls, name: str):
        pass

    @classmethod
    @abstractmethod
    async def create(cls, exercise: dict):
        pass
