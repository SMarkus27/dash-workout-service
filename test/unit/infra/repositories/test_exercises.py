from pymongo.collection import Collection

from src.infra.repositories.exercises import ExercisesRepository


def test_get_collection():
    ExercisesRepository._database_name = "test"
    ExercisesRepository._collection_name = "test"

    result = ExercisesRepository.get_collection()
    assert type(result) is Collection


def test_create_a_workout():
    ExercisesRepository._database_name = "test"
    ExercisesRepository._collection_name = "test"

    workout = {
        "name": "fly",
    }

    ExercisesRepository.create(workout)

    find = ExercisesRepository.find("fly")

    assert find is not None


def test_find_workout():
    ExercisesRepository._database_name = "test"
    ExercisesRepository._collection_name = "test"

    find = ExercisesRepository.find()

    assert find is not None