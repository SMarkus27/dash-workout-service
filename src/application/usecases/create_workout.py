from src.domain.entities.workouts import Workouts
from src.infra.repository.workout import WorkoutsRepository


class CreateWorkouts:
    def __init__(self, workout_repository: WorkoutsRepository):
        self.workout_repository = workout_repository

    def execute(self, workout: Workouts) -> None:
        valid_workout = Workouts(**workout)
        self.workout_repository.create(valid_workout.__dict__)
