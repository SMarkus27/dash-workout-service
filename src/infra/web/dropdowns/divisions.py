import pandas as pd

from src.application.usecases.find_division import GetDivision
from src.infra.repositories.division import DivisionRepository


def divisions():
    repo = DivisionRepository()
    find_divisions = GetDivision(repo)
    divisions = find_divisions.execute()
    data = pd.DataFrame(divisions)["name"]
    return data
