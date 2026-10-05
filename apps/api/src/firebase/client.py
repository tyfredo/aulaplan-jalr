from functools import lru_cache
from google.cloud.firestore import Client
from firebase_admin import firestore

@lru_cache(maxsize=1)
def get_db() -> Client:
    return firestore.client()

