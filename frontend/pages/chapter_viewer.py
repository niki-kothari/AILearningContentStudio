import streamlit as st
import requests
from ui_theme import apply_theme, logout_button, page_header, safe_text, sidebar_nav

st.set_page_config(
    page_title="Chapter Viewer",
    layout="wide"
)
apply_theme()

# =========================================================
# SESSION VALIDATION
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.warning("Please Login First")

    st.switch_page("login_fe.py")

# =========================================================
# HEADER
# =========================================================

col1, col2 = st.columns([8, 1])

with col1:
    page_header(
        "Saved Chapter Viewer",
        "Load, review, update, and download saved chapter content for the current roadmap topic."
    )

with col2:
    logout_button()

# =========================================================
# CHECK TOPIC
# =========================================================

if "topic" not in st.session_state:

    st.warning(
        "No Topic Selected"
    )

    st.info(
        "Please Generate Or Upload A Roadmap First"
    )

    if st.button("Go To Roadmap Page"):

        st.switch_page(
            "pages/roadmap_page.py"
        )

    st.stop()

# =========================================================
# DISPLAY CURRENT TOPIC
# =========================================================

topic = st.session_state.topic

st.markdown(
    f'<div class="studio-stat"><strong>{safe_text(topic)}</strong><span>Current topic</span></div>',
    unsafe_allow_html=True,
)

st.divider()

# =========================================================
# LOAD SAVED CHAPTERS
# =========================================================

try:

    response = requests.post(
        "http://127.0.0.1:5000/saved-chapters",
        json={
            "topic": topic
        }
    )

    result = response.json()

    if result["success"]:

        chapters = result["chapters"]

    else:

        st.error(
            result.get(
                "message",
                "Failed To Load Chapters"
            )
        )

        chapters = []

except Exception as e:

    st.error(f"Error : {e}")

    chapters = []

# =========================================================
# CHECK CHAPTERS
# =========================================================

if not chapters:

    st.warning(
        "No Saved Chapters Found"
    )

    if st.button("Go To Content Creator"):

        st.switch_page(
            "pages/content_page.py"
        )

    st.stop()

# =========================================================
# CLEAN CHAPTER NAMES AND SELECT CHAPTER
# =========================================================

chapter_mapping = {}

display_chapters = []

for chapter in chapters:

    original_name = chapter.replace(
        ".txt",
        ""
    )

    display_name = (
        original_name
        .replace("_", " ")
        .title()
    )

    chapter_mapping[
        display_name
    ] = original_name

    display_chapters.append(
        display_name
    )

selected_display = st.selectbox(
    "Select Saved Chapter",
    display_chapters
)

selected_chapter = chapter_mapping[
    selected_display
]

st.divider()

# =========================================================
# LOAD CHAPTER CONTENT
# =========================================================

if st.button("Load Chapter", type="primary"):

    try:

        response = requests.post(
            "http://127.0.0.1:5000/load-chapter",
            json={
                "topic": topic,
                "chapter": selected_chapter
            }
        )

        result = response.json()

        if result["success"]:

            st.session_state.viewer_content = (
                result["content"]
            )

            st.success(
                "Chapter Loaded Successfully"
            )

        else:

            st.error(
                result.get(
                    "message",
                    "Failed To Load Chapter"
                )
            )

    except Exception as e:

        st.error(f"Error : {e}")

# =========================================================
# DISPLAY CHAPTER CONTENT
# =========================================================

if "viewer_content" in st.session_state:

    st.divider()

    st.subheader(
        f"Chapter : {selected_chapter}"
    )

    edited_content = st.text_area(
        "Edit Chapter Content",
        value=st.session_state.viewer_content,
        height=500
    )

    st.session_state.viewer_content = (
        edited_content
    )

    st.divider()

    # =====================================================
    # BUTTONS
    # =====================================================

    col1, col2, col3 = st.columns(3)

    # =====================================================
    # SAVE UPDATED CONTENT
    # =====================================================

    with col1:

        if st.button("Save Updated Content", type="primary"):

            try:

                response = requests.post(
                    "http://127.0.0.1:5000/save-chapter",
                    json={
                        "topic": topic,
                        "chapter": selected_chapter,
                        "content": edited_content
                    }
                )

                result = response.json()

                if result["success"]:

                    st.success(
                        "Content Updated Successfully"
                    )

                else:

                    st.error(
                        result.get(
                            "message",
                            "Failed To Save Content"
                        )
                    )

            except Exception as e:

                st.error(f"Error : {e}")

    # =====================================================
    # DOWNLOAD CONTENT
    # =====================================================

    with col2:
        if edited_content:

            st.download_button(
                label="Download Chapter",
                data=edited_content,
                file_name=f"{selected_chapter}.txt",
                mime="text/plain"
            )

        else:
            st.warning(
                "No Content Available To Download"
            )

    # =====================================================
    # CLEAR VIEWER
    # =====================================================

    with col3:

        if st.button("Clear Viewer"):

            del st.session_state.viewer_content

            st.rerun()

# =========================================================
# NAVIGATION BUTTONS
# =========================================================

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button("Go To Content Creator"):

        st.switch_page(
            "pages/content_page.py"
        )

with col2:

    if st.button("Go To Dashboard"):

        st.switch_page(
            "pages/dashboard_fe.py"
        )

# =========================================================
# SIDEBAR
# =========================================================

sidebar_nav()

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI Content Studio | Chapter Management System"
)
