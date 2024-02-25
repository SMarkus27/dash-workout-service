from pymongo.collection import Collection

from src.infra.repositories.division import DivisionRepository


def test_get_collection():
    DivisionRepository._database_name = "test"
    DivisionRepository._collection_name = "test"

    result = DivisionRepository.get_collection()
    assert type(result) is Collection


def test_create_a_workout():
    DivisionRepository._database_name = "test"
    DivisionRepository._collection_name = "test"

    workout = {
        "name": "chest",
    }

    DivisionRepository.create(workout)

    find = DivisionRepository.find("chest")

    assert find is not None


def test_find_workout():
    DivisionRepository._database_name = "test"
    DivisionRepository._collection_name = "test"

    find = DivisionRepository.find()

    assert find is not None
