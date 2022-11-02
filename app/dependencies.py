from fastapi import Depends
from app.service.activity import ActivityService
from app.service.mongo import SingletonMongo

mongo = SingletonMongo()

def get_mongo_client() -> SingletonMongo:
    return mongo

def get_activity_service(mongo_client: SingletonMongo = Depends(get_mongo_client)) -> ActivityService:
    return ActivityService(mongo_client)


