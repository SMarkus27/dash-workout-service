from src.infra.repositories.exercises import ExercisesRepository


class GetExercises:
    def __init__(self, exercises_repository: ExercisesRepository):
        self.exercises_repository = exercises_repository

    def execute(self):
        return self.exercises_repository.find()
