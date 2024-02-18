from src.infra.repositories.division import DivisionRepository


class GetDivision:
    def __init__(self, division_repository: DivisionRepository):
        self.division_repository = division_repository

    def execute(self):
        return self.division_repository.find()


