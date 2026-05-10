import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MajorFit",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

html, body, .stApp {
    margin: 0 !important;
    padding: 0 !important;
    background: #0C0C14 !important;
}

.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}

[data-testid="stAppViewContainer"] {
    padding: 0 !important;
    margin: 0 !important;
}

[data-testid="stVerticalBlock"] {
    gap: 0 !important;
}

iframe {
    width: 100vw !important;
    height: 100vh !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

with open("majorfit.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(
    html_code,
    height=900,
    scrolling=True
)