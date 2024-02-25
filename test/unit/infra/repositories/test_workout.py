from pymongo.collection import Collection

from src.infra.repositories.workout import WorkoutsRepository


def test_get_collection():
    WorkoutsRepository._database_name= "test"
    WorkoutsRepository._collection_name= "test"

    result = WorkoutsRepository.get_collection()
    assert type(result) is Collection


def test_create_a_workout():
    WorkoutsRepository._database_name = "test"
    WorkoutsRepository._collection_name = "test"

    workout = {
        "date": "2021-01-22",
        "name": "fly",
        "weight": 55,
        "type": "chest"
    }

    WorkoutsRepository.create(workout)

    find = WorkoutsRepository.find("chest")

    assert find is not None


def test_find_workout():
    WorkoutsRepository._database_name = "test"
    WorkoutsRepository._collection_name = "test"

    find = WorkoutsRepository.find("chest")

    assert find is not None

