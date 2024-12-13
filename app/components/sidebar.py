import datetime

import streamlit as st
import streamlit_cookies_controller as stc
from business_logic.auth import Authentication

auth = Authentication()
cookies_controller = stc.CookieController()


# Helper functions
def display_error(message):
    st.sidebar.error(message)


def display_success(message):
    st.sidebar.success(message)


def set_user_cookie(user):
    current_time = datetime.datetime.now()
    expires_in_seconds = int(user["expiresIn"])
    expires = current_time + datetime.timedelta(seconds=expires_in_seconds)
    cookies_controller.set("user", user, expires=expires)


# Business logic
def create_user(username, password):
    if not username or not password:
        display_error("Username and password are required")
        return

    new_user = auth.create_user(username, password)
    if new_user is None:
        display_error("Error creating account")
    else:
        st.sidebar.success(f"Account created for {username}")


def login(username, password):
    if not username or not password:
        display_error("Username and password are required")
        return

    auth_user = auth.authenticate(username, password)
    if auth_user is None:
        st.sidebar.error("Invalid credentials")
    else:
        user = {
            "idToken": auth_user["idToken"],
            "refreshToken": auth_user["refreshToken"],
            "email": auth_user["email"],
        }
        st.session_state["user"] = user
        set_user_cookie(user)

        st.rerun()


def logout():
    if "user" in st.session_state:
        del st.session_state["user"]
        cookies_controller.remove("user")
        st.rerun()


# UI
def sidebar():
    if "user" in st.session_state:
        st.sidebar.button("Logout", on_click=logout)
    else:
        # Login form
        st.sidebar.text_input("Username", key="login_username")
        st.sidebar.text_input("Password", type="password", key="login_password")
        st.sidebar.button(
            "Login",
            on_click=lambda: login(
                st.session_state["login_username"],
                st.session_state["login_password"],
            ),
        )

        st.sidebar.divider()

        # Create user form
        st.sidebar.markdown("Don't have an account? Create one")
        st.sidebar.text_input("New Username", key="create_username")
        st.sidebar.text_input("New Password", type="password", key="create_password")
        st.sidebar.button(
            "Create Account",
            on_click=lambda: create_user(
                st.session_state["create_username"],
                st.session_state["create_password"],
            ),
        )
