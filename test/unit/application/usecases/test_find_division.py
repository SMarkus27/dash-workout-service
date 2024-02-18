from src.application.usecases.find_division import GetDivision
from test.unit.db_test import MongoDBTest


def test_should_find_a_division():
    repo_test = MongoDBTest()
    find = GetDivision(repo_test)

    result = find.execute()

    assert result is not None

