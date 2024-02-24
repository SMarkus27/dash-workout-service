from src.application.usecases.find_workout import GetWorkout
from test.unit.db_test import MongoDBTest


def test_should_find_a_workout():
    repo_test = MongoDBTest()
    find = GetWorkout(repo_test)

    result = find.execute("chest")

    assert result is not None

