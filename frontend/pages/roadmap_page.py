import json
import streamlit as st
import requests
from ui_theme import apply_theme, logout_button, page_header, safe_text, sidebar_nav

st.set_page_config(
    page_title="Roadmap Creator",
    layout="wide"
)
apply_theme()

# =========================================================
# SESSION VALIDATION
# =========================================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.switch_page("login_fe.py")

# =========================================================
# HEADER
# =========================================================

col1, col2 = st.columns([8, 1])

with col1:
    page_header(
        "Roadmap Creator",
        "Generate a structured learning roadmap or upload an existing JSON plan to continue content production."
    )

with col2:
    logout_button()

# =========================================================
# MODEL SELECTION
# =========================================================

model_name = st.selectbox(
    "Select AI Model",
    [
        "openai",
        "gemini"
    ]
)

st.session_state.model = model_name

# =========================================================
# OPTION SELECTION
# =========================================================

option = st.radio(
    "Choose Option",
    [
        "Generate New Roadmap",
        "Upload Existing Roadmap"
    ]
)

st.divider()

# =========================================================
# GENERATE ROADMAP
# =========================================================

if option == "Generate New Roadmap":

    topic = st.text_input(
        "Enter Topic",
        placeholder="Example : Python Programming"
    )

    if st.button("Generate Roadmap", type="primary"):

        if not topic.strip():

            st.error("Please Enter Topic")

            st.stop()

        with st.spinner("Generating Roadmap..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:5000/generate-roadmap",
                    json={
                        "topic": topic,
                        "model": model_name
                    }
                )

                result = response.json()

                if result["success"]:

                    st.session_state.topic = topic

                    st.session_state.roadmap = (
                        result["roadmap"]
                    )

                    st.success(
                        "Roadmap Generated Successfully"
                    )

                else:

                    st.error(
                        result.get(
                            "message",
                            "Roadmap Generation Failed"
                        )
                    )

            except Exception as e:

                st.error(f"Error : {e}")

# =========================================================
# UPLOAD ROADMAP
# =========================================================

elif option == "Upload Existing Roadmap":

    uploaded_file = st.file_uploader(
        "Upload Roadmap JSON File",
        type=["json"]
    )

    if uploaded_file is not None:

        try:

            roadmap_json = json.load(
                uploaded_file
            )

            st.session_state.roadmap = (
                roadmap_json
            )

            st.session_state.topic = (
                roadmap_json["topic"]
            )

            st.success(
                "Roadmap Uploaded Successfully"
            )

        except Exception as e:

            st.error(
                f"Invalid JSON File : {e}"
            )

# =========================================================
# DISPLAY ROADMAP
# =========================================================

if "roadmap" in st.session_state:

    st.divider()

    st.subheader("Generated Roadmap")

    chapters = st.session_state.roadmap.get("chapters", [])
    topic_label = safe_text(st.session_state.topic)
    st.markdown(
        f'<div class="studio-stat"><strong>{len(chapters)}</strong><span>Chapters prepared for {topic_label}</span></div>',
        unsafe_allow_html=True,
    )

    st.json(
        st.session_state.roadmap
    )

    st.divider()

    # =====================================================
    # BUTTONS
    # =====================================================

    col1, col2 = st.columns(2)

    # =====================================================
    # SAVE ROADMAP
    # =====================================================

    with col1:

        if st.button("Save Roadmap", type="primary"):

            try:

                response = requests.post(
                    "http://127.0.0.1:5000/save-roadmap",
                    json={
                        "topic": st.session_state.topic,
                        "roadmap": st.session_state.roadmap
                    }
                )

                result = response.json()

                if result["success"]:

                    st.success(
                        "Roadmap Saved Successfully"
                    )

                else:

                    st.error(
                        result.get(
                            "message",
                            "Failed To Save Roadmap"
                        )
                    )

            except Exception as e:

                st.error(f"Error : {e}")

    # =====================================================
    # DOWNLOAD ROADMAP
    # =====================================================

    with col2:

        roadmap_json_string = json.dumps(
            st.session_state.roadmap,
            indent=4
        )

        st.download_button(
            label="Download Roadmap",
            data=roadmap_json_string,
            file_name=f"{st.session_state.topic}.json",
            mime="application/json"
        )

    st.divider()

    # =====================================================
    # CONTENT PAGE
    # =====================================================

    if st.button("Go To Content Creator", type="primary"):

        st.switch_page(
            "pages/content_page.py"
        )

sidebar_nav()

