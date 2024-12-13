import streamlit as st
import streamlit_cookies_controller as stc
from components.sidebar import sidebar

cookies_controller = stc.CookieController()


def get_user_from_cookies() -> None:
    """Get user from cookies and set it to session state."""
    user_cookie = cookies_controller.get("user")
    if user_cookie:
        st.session_state["user"] = user_cookie


def setup_navigation() -> st.navigation:
    """Set up navigation based on user's authentication status."""
    if "user" not in st.session_state:
        return st.navigation([st.Page("app_pages/unauthenticated_page.py")])
    return st.navigation([st.Page("app_pages/authenticated_page.py")])


if "user" not in st.session_state:
    get_user_from_cookies()

pages = setup_navigation()
pages.run()


# Sidebar UI
sidebar()
