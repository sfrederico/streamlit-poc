import requests
import streamlit as st


class Authentication:
    """Class to handle user authentication."""

    firebase_api_key: str

    def __init__(self) -> None:
        """Initialize the class."""
        self.firebase_api_key = st.secrets["firebase_api_key"]

    def create_user(self, email: str, password: str) -> dict:
        """Create a new user in Firebase Authentication."""
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.firebase_api_key}"
        data = {"email": email, "password": password, "returnSecureToken": True}
        response = requests.post(url, json=data, timeout=10)
        if response.ok:
            return response.json()
        return None

    def authenticate(self, email: str, password: str) -> dict:
        """Authenticate a user in Firebase Authentication."""
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.firebase_api_key}"
        data = {"email": email, "password": password, "returnSecureToken": True}
        response = requests.post(url, json=data, timeout=10)
        if response.ok:
            return response.json()
        return None
