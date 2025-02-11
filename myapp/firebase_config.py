import firebase_admin
from firebase_admin import credentials, firestore

FIREBASE_CREDENTIALS = r"myapp\Dso.json"

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred)

db = firestore.client()
