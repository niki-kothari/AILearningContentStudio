import streamlit as st
import requests
from ui_theme import apply_theme

st.set_page_config(page_title="AI Content Studio", layout="centered")
apply_theme()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.switch_page("pages/dashboard_fe.py")

st.markdown(
    """
    <div class="studio-login">
        <div class="studio-eyebrow">Secure Workspace</div>
        <h1 class="studio-title">AI Content Studio</h1>
        <p class="studio-subtitle">Sign in to create roadmaps, generate chapters, and manage saved learning content.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login", type="primary"):

    response = requests.post(
        "http://127.0.0.1:5000/login",
        json={
            "username": username,
            "password": password
        }
    )

    result = response.json()

    if result["success"]:
        st.session_state.logged_in = True
        st.success("Login Successful")
        #st.switch_page("pages/roadmap_page.py")
        st.switch_page("pages/dashboard_fe.py")

    else:
        st.error(result["message"])

