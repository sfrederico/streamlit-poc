import streamlit as st

from auth import Authentication

auth = Authentication()

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
submit = st.sidebar.button("Login")

st.text_area("Welcome to the app!")

st.sidebar.divider()

st.sidebar.markdown("Don't have an account? Create one")
new_username = st.sidebar.text_input("New Username")
new_password = st.sidebar.text_input("New Password", type="password")
new_submit = st.sidebar.button("Create Account")


if new_submit:
    auth.create_user(new_username, new_password)
    st.sidebar.success(f"Account created for {new_username}")
