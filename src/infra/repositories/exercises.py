# Third-Party Library
from decouple import config

from src.application.interfaces.repositories.exercises import IExercisesRepository
from src.infra.database.mongodb import MongoDBInfrastructure


class ExercisesRepository(IExercisesRepository):

    _database_name = config("MONGODB_DATABASE_NAME")
    _collection_name = config("MONGODB_EXERCISES_COLLECTION")

    @classmethod
    def get_collection(cls):
        mongodb_client = MongoDBInfrastructure.get_client()
        database = mongodb_client[cls._database_name]
        collection = database[cls._collection_name]
        return collection

    @classmethod
    def create(cls, exercise: dict):
        mongo_cliente = cls.get_collection()
        mongo_cliente.insert_one(exercise)

    @classmethod
    def find(cls, exercise: str = None):
        mongo_cliente = cls.get_collection()
        result = mongo_cliente.find({}, {"_id": False})
        return list(result)
