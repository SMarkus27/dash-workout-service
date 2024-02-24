from abc import ABC, abstractmethod


class IWorkoutsRepository(ABC):
    @classmethod
    @abstractmethod
    async def find(cls, name: str):
        pass

    @classmethod
    @abstractmethod
    async def create(cls, workouts: dict):
        pass
