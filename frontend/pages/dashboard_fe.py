import streamlit as st
from ui_theme import apply_theme, logout_button, page_header, safe_text, sidebar_nav

st.set_page_config(
    page_title="AI Content Studio",
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
        "Dashboard",
        "Plan course roadmaps, generate chapter content, and keep your saved learning material organized."
    )

with col2:
    logout_button()

# =========================================================
# WELCOME SECTION
# =========================================================

stat1, stat2, stat3 = st.columns(3)

with stat1:
    st.markdown(
        '<div class="studio-stat"><strong>3</strong><span>Core workflows</span></div>',
        unsafe_allow_html=True,
    )

with stat2:
    topic_label = safe_text(st.session_state.get("topic", "Not selected"))
    st.markdown(
        f'<div class="studio-stat"><strong>{topic_label}</strong><span>Current topic</span></div>',
        unsafe_allow_html=True,
    )

with stat3:
    roadmap_state = "Ready" if "roadmap" in st.session_state else "Pending"
    st.markdown(
        f'<div class="studio-stat"><strong>{roadmap_state}</strong><span>Roadmap status</span></div>',
        unsafe_allow_html=True,
    )

# =========================================================
# MAIN OPTIONS
# =========================================================

st.subheader("Choose Your Workflow")

option = st.radio(
    "Select Option",
    [
        "Roadmap Creator",
        "Chapter Content Creator",
        "View Saved Chapters"
    ]
)

st.divider()

# =========================================================
# ROADMAP CREATOR
# =========================================================

if option == "Roadmap Creator":

    st.markdown(
        '<div class="studio-card"><h3>Roadmap Creator</h3><p>Create a new AI roadmap or upload an existing JSON roadmap for a course topic.</p></div>',
        unsafe_allow_html=True,
    )

    if st.button("Open Roadmap Creator", type="primary"):

        st.switch_page(
            "pages/roadmap_page.py"
        )

# =========================================================
# CONTENT CREATOR
# =========================================================

elif option == "Chapter Content Creator":

    st.markdown(
        '<div class="studio-card"><h3>Chapter Content Creator</h3><p>Generate, upload, edit, save, and download chapter-wise course content.</p></div>',
        unsafe_allow_html=True,
    )

    # Check roadmap exists

    if "roadmap" not in st.session_state:

        st.warning("""
        Please Generate Or Upload A Roadmap First
        """)

    else:

        if st.button("Open Content Creator", type="primary"):

            st.switch_page(
                "pages/content_page.py"
            )

# =========================================================
# VIEW SAVED CHAPTERS
# =========================================================

elif option == "View Saved Chapters":

    st.markdown(
        '<div class="studio-card"><h3>Saved Chapters</h3><p>Review and update chapter files already stored for the active topic.</p></div>',
        unsafe_allow_html=True,
    )

    if st.button("Open Chapter Viewer", type="primary"):

        st.switch_page(
            "pages/chapter_viewer.py"
        )

st.divider()

# =========================================================
# SIDEBAR
# =========================================================

sidebar_nav()

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI Content Studio | Flask + Streamlit + LangChain + LangGraph"
)

