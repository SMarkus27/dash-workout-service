# Standard Library
from dataclasses import dataclass


@dataclass
class Workouts:
    date: str
    name: str
    weight: float
    type: str

    def __post_init__(self):
        self.validate_name(self.name)
        self.validate_weight(self.weight)
        self.validate_type(self.type)

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

