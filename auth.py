import firebase_admin
from firebase_admin import auth, credentials


class Authentication:
    def __init__(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate("./admin-sdk-key-ee2968.json")
            firebase_admin.initialize_app(cred)

    def create_user(self, email, password):
        user = auth.create_user(email=email, password=password)
        return user
