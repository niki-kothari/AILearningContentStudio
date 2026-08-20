import streamlit as st
import requests
from ui_theme import apply_theme, logout_button, page_header, safe_text, sidebar_nav

st.set_page_config(
    page_title="Content Creator",
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
# CHECK ROADMAP
# =========================================================

if "roadmap" not in st.session_state:

    st.warning(
        "Please Generate Or Upload Roadmap First"
    )

    st.switch_page(
        "pages/roadmap_page.py"
    )

# =========================================================
# HEADER
# =========================================================

col1, col2 = st.columns([8, 1])

with col1:
    page_header(
        "Chapter Content Creator",
        "Turn roadmap chapters into editable course content, then save or download polished chapter files."
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
        "gemini",
        "groq"
    ]
)

# Store selected model
st.session_state.model = model_name

# =========================================================
# TOPIC
# =========================================================

st.markdown(
    f'<div class="studio-stat"><strong>{safe_text(st.session_state.topic)}</strong><span>Active topic</span></div>',
    unsafe_allow_html=True,
)

# =========================================================
# VIEW ROADMAP
# =========================================================

with st.expander("View Roadmap"):

    st.write(
        st.session_state.roadmap
    )

# =========================================================
# EXTRACT CHAPTERS TITLES
# =========================================================

chapters = []

for chapter in st.session_state.roadmap["chapters"]:

    chapters.append(
        chapter["chapter_title"]
    )

# Remove duplicates
chapters = list(dict.fromkeys(chapters))

# =========================================================
# SELECT CHAPTER
# =========================================================

selected_chapter = st.selectbox(
    "Select Chapter",
    chapters
)

st.divider()

# =========================================================
# GET SELECTED CHAPTER SUBTOPICS
# =========================================================

selected_subtopics = []

for chapter in st.session_state.roadmap["chapters"]:

    if chapter["chapter_title"] == selected_chapter:

        selected_subtopics = chapter["subtopics"]

        break

# =========================================================
# DISPLAY CHAPTER SUBTOPICS
# =========================================================

st.subheader("Chapter Subtopics")

for topic in selected_subtopics:

    st.markdown(
        f'<div class="studio-subtopic">{safe_text(topic)}</div>',
        unsafe_allow_html=True,
    )

st.divider()

# =========================================================
# OPTION SELECTION
# =========================================================

option = st.radio(
    "Choose Option",
    [
        "Generate New Content",
        "Upload Existing Content"
    ]
)

# =========================================================
# INITIALIZE CONTENT
# =========================================================

if "chapter_content" not in st.session_state:
    st.session_state.chapter_content = ""

# =========================================================
# OPTION 1 : GENERATE NEW CONTENT
# =========================================================

if option == "Generate New Content":

    if st.button("Generate Chapter Content", type="primary"):

        with st.spinner(
            "Generating Chapter Content..."
        ):

            try:

                response = requests.post(
                    "http://127.0.0.1:5000/generate-chapter",
                    json={
                        "topic": st.session_state.topic,
                        "chapter": selected_chapter,
                        "subtopics": selected_subtopics,
                        "model": st.session_state.model
                    }
                )

                result = response.json()

                if result["success"]:

                    st.session_state.chapter_content = (
                        result["content"]
                    )

                    st.success(
                        "Content Generated Successfully"
                    )

                else:
                    st.error(
                        result.get(
                            "message",
                            "Failed To Generate Content"
                        )
                    )
            except Exception as e:

                st.error(f"Error : {e}")

# =========================================================
# OPTION 2 : UPLOAD EXISTING CONTENT
# =========================================================

elif option == "Upload Existing Content":

    uploaded_content = st.file_uploader(
        "Upload Chapter Content",
        type=["txt"]
    )

    if uploaded_content is not None:

        content_text = (
            uploaded_content.read().decode("utf-8")
        )

        st.session_state.chapter_content = (
            content_text
        )

        st.success(
            "Content Uploaded Successfully"
        )

# =========================================================
# DISPLAY / EDIT CONTENT
# =========================================================

if st.session_state.chapter_content:

    st.divider()

    st.subheader(
        f"Chapter : {selected_chapter}"
    )

    edited_content = st.text_area(
        "Edit Content",
        value=st.session_state.chapter_content,
        height=500
    )

    st.session_state.chapter_content = (
        edited_content
    )

    st.divider()

    # =====================================================
    # BUTTONS
    # =====================================================

    col1, col2, col3 = st.columns(3)

    # =====================================================
    # SAVE CONTENT
    # =====================================================

    with col1:

        if st.button("Save Content", type="primary"):

            try:

                response = requests.post(
                    "http://127.0.0.1:5000/save-chapter",
                    json={
                        "topic": st.session_state.topic,
                        "chapter": selected_chapter,
                        "content": edited_content
                    }
                )

                result = response.json()

                if result["success"]:

                    st.success(
                        "Content Saved Successfully"
                    )

                else:

                    st.error(
                        "Failed To Save Content"
                    )

            except Exception as e:

                st.error(f"Error : {e}")

    # =====================================================
    # DOWNLOAD CONTENT
    # =====================================================

    with col2:

        st.download_button(
            label="Download Content",
            data=edited_content,
            file_name=f"{selected_chapter}.txt",
            mime="text/plain"
        )

    # =====================================================
    # CLEAR CONTENT
    # =====================================================

    with col3:

        if st.button("Clear Content"):

            st.session_state.chapter_content = ""

            st.rerun()

# =========================================================
# VIEW SAVED CHAPTERS
# =========================================================

st.divider()

if st.button("View Saved Chapters", type="primary"):

    st.switch_page(
        "pages/chapter_viewer.py"
    )

# =========================================================
# BACK BUTTON
# =========================================================

if st.button("Back To Roadmap Page"):

    st.switch_page(
        "pages/roadmap_page.py"
    )

sidebar_nav()
