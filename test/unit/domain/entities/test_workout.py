import pytest

from src.domain.entities.workouts import Workouts


def test_valid_workout():
    workout = {
        "date": "2021-01-22",
        "name": "fly",
        "weight": 55,
        "type": "chest"
    }
    Workouts(**workout)

    assert workout["name"] == "fly"
    assert workout["date"] == "2021-01-22"
    assert workout["weight"] == 55
    assert workout["type"] == "chest"


def test_must_throw_name_invalid():
    workout = {
        "date": "2021-01-22",
        "name": "fl",
        "weight": 55,
        "type": "chest"
    }

    with pytest.raises(ValueError) as error:
        Workouts(**workout)

    assert "Exercise name must be at least 3 characters" in str(error.value)


def test_must_throw_weight_invalid():
    workout = {
        "date": "2021-01-22",
        "name": "fly",
        "weight": -55,
        "type": "chest"
    }

    with pytest.raises(ValueError) as error:
        Workouts(**workout)

    assert "Weight must be a positive value" in str(error.value)


def test_must_throw_exercise_type_invalid():
    workout = {
        "date": "2021-01-22",
        "name": "fly",
        "weight": 55,
        "type": "che"
    }

    with pytest.raises(ValueError) as error:
        Workouts(**workout)

    assert "Exercise type must be at least 5 characters" in str(error.value)
