# Third-Party Library
import pandas as pd

from src.application.usecases.find_workout import GetWorkout
from src.infra.repositories.workout import WorkoutsRepository
from src.infra.web.layouts.bar import build_figure


def plot(exercise_type: str):
    repo = WorkoutsRepository()
    find_workouts = GetWorkout(repo)
    workouts = find_workouts.execute(exercise_type)
    data = pd.DataFrame(workouts)
    figure = build_figure(data)
    return figure
