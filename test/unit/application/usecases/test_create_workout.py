from src.application.usecases.create_workout import CreateWorkouts
from test.unit.db_test import MongoDBTest


def test_should_create_a_workout():
    repo_test = MongoDBTest()
    create = CreateWorkouts(repo_test)

    workout = {
        "date": "2021-01-22",
        "name": "fly",
        "weight": 55,
        "type": "chest"
    }

    create.execute(workout)

    result = repo_test.find("chest")
    assert result is not None



