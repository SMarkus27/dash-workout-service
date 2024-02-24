# Third-Party Libraries
from decouple import config
from pymongo import MongoClient


class MongoDBInfrastructure:
    mongodb_client: MongoClient = None
    _mongodb_url: str = config("MONGODB_STRING_CONNECTION")

    @classmethod
    def get_client(cls):
        if cls.mongodb_client is None:
            cls.mongodb_client = MongoClient(cls._mongodb_url)

        return cls.mongodb_client
