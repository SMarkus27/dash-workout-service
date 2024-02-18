from src.application.usecases.find_exercises import GetExercises
from test.unit.db_test import MongoDBTest


def test_should_find_a_exercises():
    repo_test = MongoDBTest()
    find = GetExercises(repo_test)

    result = find.execute()

    assert result is not None

