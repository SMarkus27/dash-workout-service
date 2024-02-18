from src.infra.repository.workout import WorkoutsRepository


class GetWorkout:
    def __init__(self, workout_repository: WorkoutsRepository):
        self.workout_repository = workout_repository

    def execute(self, workout_type: str):
        return self.workout_repository.find(workout_type)
