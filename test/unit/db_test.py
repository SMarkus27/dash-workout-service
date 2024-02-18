from src.infra.database.mongodb import MongoDBInfrastructure


class MongoDBTest:

    _database_name = "test"
    _collection_name = "test"

    @classmethod
    def get_collection(cls):
        mongodb_client = MongoDBInfrastructure.get_client()
        database = mongodb_client[cls._database_name]
        collection = database[cls._collection_name]
        return collection

    @classmethod
    def create(cls, workout: dict):
        mongo_cliente = cls.get_collection()
        mongo_cliente.insert_one(workout)

    @classmethod
    def find(cls, workout_type: str = None):
        mongo_cliente = cls.get_collection()
        result = mongo_cliente.find({"type": workout_type}, {"_id": False})
        return list(result)