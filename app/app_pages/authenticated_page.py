import streamlit as st

user = st.session_state.get("user", None)

st.title(f"Welcome {user['email']}!")
st.caption("You are currently logged in.")
