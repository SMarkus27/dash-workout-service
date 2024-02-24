import pandas as pd

from src.application.usecases.find_exercises import GetExercises
from src.infra.repositories.exercises import ExercisesRepository


def exercises():
    repo = ExercisesRepository()
    find_exercises = GetExercises(repo)
    exercises = find_exercises.execute()
    data = pd.DataFrame(exercises)["name"]
    return data
