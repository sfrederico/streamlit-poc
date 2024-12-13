import requests
import streamlit as st


class Authentication:
    firebase_api_key: str

    def __init__(self):
        self.firebase_api_key = st.secrets["firebase_api_key"]

    def create_user(self, email, password):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.firebase_api_key}"
        data = {"email": email, "password": password, "returnSecureToken": True}
        response = requests.post(url, json=data)
        if response.ok:
            return response.json()
        return None

    def authenticate(self, email, password):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.firebase_api_key}"
        data = {"email": email, "password": password, "returnSecureToken": True}
        response = requests.post(url, json=data)
        if response.ok:
            return response.json()
        return None
