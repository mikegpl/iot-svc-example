from dataclasses import asdict, dataclass, field
from datetime import datetime

from app.service.mongo import SingletonMongo

@dataclass
class DeviceActivity:
    time: datetime
    device: str = "anjay"
    activity_type: str = "register"

@dataclass
class TimeRange:
    start: datetime
    end: datetime

class ActivityService():
    def __init__(self, client: SingletonMongo) -> None:
        self.client = client()
        self.collection = self.client['coiote']['activity']

    def purge_activities(self):
        self.collection.delete_many(filter={})

    def get_for_device(self, device: str): 
        return [DeviceActivity(**db_device) for db_device in self.collection.find(filter={"device": device})]

    def log_activity(self, activity: DeviceActivity):
        self.collection.insert_one(asdict(activity))

    def unique_devices(self, time_range: TimeRange):
        raise NotImplementedError(f"This method should return number of unique device IDs in range {asdict(time_range)}")