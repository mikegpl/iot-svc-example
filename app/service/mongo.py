
from threading import Lock
from typing import Optional

from pymongo_inmemory import MongoClient


class SingletonMongo():
    def __init__(self):
        self._client: Optional[MongoClient] = None
        self._lock = Lock()

    def __call__(self):
        if self._client is not None:
            return self._client

        with self._lock:
            if self._client is not None:
                return self._client
            self._client = MongoClient()

        return self._client

    def close(self):
        if self._client is not None:
            self._client.close()
