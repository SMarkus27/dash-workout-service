# Standard Library
from dataclasses import dataclass


@dataclass
class Workouts:
    _date: str
    _name: str
    _weight: float
    _type: str

    def __post_init__(self):
        self.validate_name(self._name)
        self.validate_weight(self._weight)
        self.validate_type(self._type)

    @staticmethod
    def validate_name(name: str):
        if len(name) < 3:
            raise ValueError("Exercise name must be at least 3 characters")

    @staticmethod
    def validate_weight(weight: float):
        if weight < 0:
            raise ValueError("Weight must be a positive value")

    @staticmethod
    def validate_type(type: str):
        if len(type) < 5:
            raise ValueError("Exercise type must be at least 5 characters")

