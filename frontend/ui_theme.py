from html import escape

import streamlit as st


def safe_text(value):
    return escape(str(value), quote=True)


def apply_theme():
    st.markdown(
        """
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            :root {
                --studio-primary: #2563eb;
                --studio-primary-dark: #1e40af;
                --studio-accent: #14b8a6;
                --studio-ink: #172033;
                --studio-muted: #667085;
                --studio-border: #d9e2ef;
                --studio-surface: #ffffff;
                --studio-bg: #f3f6fb;
            }

            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(37, 99, 235, 0.10), transparent 32rem),
                    linear-gradient(180deg, #f8fbff 0%, var(--studio-bg) 100%);
                color: var(--studio-ink);
            }

            .main .block-container {
                max-width: 1180px;
                padding-top: 1.7rem;
                padding-bottom: 2.5rem;
            }

            [data-testid="stSidebar"] {
                background: #0f172a;
            }

            [data-testid="stSidebar"] * {
                color: #e5edf8 !important;
            }

            [data-testid="stSidebar"] .stButton > button {
                border-color: rgba(255, 255, 255, 0.16);
                background: rgba(255, 255, 255, 0.08);
            }

            h1, h2, h3 {
                color: var(--studio-ink);
                letter-spacing: 0;
            }

            h1 {
                font-size: 2.15rem !important;
                font-weight: 800 !important;
            }

            h2, h3 {
                font-weight: 750 !important;
            }

            div[data-testid="stExpander"] {
                border-color: var(--studio-border) !important;
                border-radius: 8px !important;
                box-shadow: 0 16px 42px rgba(15, 23, 42, 0.06);
            }

            .stButton > button,
            .stDownloadButton > button,
            button[kind="primary"] {
                width: 100%;
                min-height: 2.7rem;
                border-radius: 8px;
                border: 1px solid var(--studio-primary);
                background: var(--studio-primary);
                color: #ffffff;
                font-weight: 700;
                box-shadow: 0 10px 22px rgba(37, 99, 235, 0.18);
                transition: all 160ms ease;
            }

            .stButton > button:hover,
            .stDownloadButton > button:hover {
                border-color: var(--studio-primary-dark);
                background: var(--studio-primary-dark);
                color: #ffffff;
                transform: translateY(-1px);
            }

            .stTextInput input,
            .stTextArea textarea,
            .stSelectbox div[data-baseweb="select"] > div,
            .stFileUploader section {
                border-radius: 8px !important;
                border-color: var(--studio-border) !important;
                background: #ffffff !important;
            }

            .stRadio [role="radiogroup"] {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
                gap: 0.75rem;
            }

            .stRadio label {
                min-height: 3rem;
                padding: 0.65rem 0.8rem;
                border: 1px solid var(--studio-border);
                border-radius: 8px;
                background: #ffffff;
            }

            .studio-hero {
                padding: 1.35rem 1.5rem;
                border: 1px solid var(--studio-border);
                border-radius: 8px;
                background:
                    linear-gradient(135deg, rgba(37, 99, 235, 0.10), rgba(20, 184, 166, 0.08)),
                    #ffffff;
                box-shadow: 0 18px 48px rgba(15, 23, 42, 0.08);
                margin-bottom: 1.1rem;
            }

            .studio-eyebrow {
                margin-bottom: 0.35rem;
                color: var(--studio-primary);
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            }

            .studio-title {
                margin: 0;
                color: var(--studio-ink);
                font-size: clamp(1.7rem, 3vw, 2.55rem);
                font-weight: 850;
                line-height: 1.08;
            }

            .studio-subtitle {
                max-width: 760px;
                margin: 0.55rem 0 0;
                color: var(--studio-muted);
                font-size: 1.02rem;
                line-height: 1.6;
            }

            .studio-card {
                height: 100%;
                padding: 1.05rem;
                border: 1px solid var(--studio-border);
                border-radius: 8px;
                background: var(--studio-surface);
                box-shadow: 0 16px 38px rgba(15, 23, 42, 0.06);
            }

            .studio-card h3 {
                margin: 0 0 0.45rem;
                font-size: 1.05rem;
            }

            .studio-card p,
            .studio-muted {
                color: var(--studio-muted);
                line-height: 1.55;
            }

            .studio-stat {
                padding: 0.85rem 1rem;
                border-left: 4px solid var(--studio-accent);
                border-radius: 8px;
                background: #ffffff;
                box-shadow: 0 12px 28px rgba(15, 23, 42, 0.05);
                margin-bottom: 0.75rem;
            }

            .studio-stat strong {
                display: block;
                overflow-wrap: anywhere;
                font-size: 1.35rem;
                color: var(--studio-ink);
            }

            .studio-stat span {
                color: var(--studio-muted);
                font-size: 0.9rem;
            }

            .studio-subtopic {
                padding: 0.65rem 0.8rem;
                border: 1px solid var(--studio-border);
                border-radius: 8px;
                background: #ffffff;
                color: var(--studio-ink);
                margin-bottom: 0.45rem;
            }

            .studio-login {
                max-width: 460px;
                margin: 3.5rem auto 0;
                padding: 1.5rem;
                border: 1px solid var(--studio-border);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.94);
                box-shadow: 0 22px 60px rgba(15, 23, 42, 0.12);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title, subtitle="", eyebrow="AI Content Studio"):
    st.markdown(
        f"""
        <section class="studio-hero">
            <div class="studio-eyebrow">{safe_text(eyebrow)}</div>
            <h1 class="studio-title">{safe_text(title)}</h1>
            <p class="studio-subtitle">{safe_text(subtitle)}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def sidebar_nav():
    st.sidebar.markdown("### AI Content Studio")
    st.sidebar.caption("Flask backend + Streamlit workspace")

    if "topic" in st.session_state:
        st.sidebar.markdown(f"**Topic:** {st.session_state.topic}")

    if st.sidebar.button("Dashboard"):
        st.switch_page("pages/dashboard_fe.py")

    if st.sidebar.button("Roadmap Creator"):
        st.switch_page("pages/roadmap_page.py")

    if st.sidebar.button("Content Creator"):
        if "roadmap" not in st.session_state:
            st.sidebar.warning("Generate or upload a roadmap first.")
        else:
            st.switch_page("pages/content_page.py")

    if st.sidebar.button("Chapter Viewer"):
        st.switch_page("pages/chapter_viewer.py")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.switch_page("login_fe.py")


def logout_button():
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.switch_page("login_fe.py")
