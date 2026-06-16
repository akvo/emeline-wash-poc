import streamlit as st
import os

st.set_page_config(
    page_title="Akvo · Water project PoC",
    page_icon="💧",
    layout="wide",
)

SECTIONS = {
    "PoC": [
        {"name": "Unique WASH ID · PoC",        "file": "unique_wash_id.html"},
        {"name": "WaterConnect · Demo",        "file": "WaterConnect_Demo_Mock.html"},
        {"name": "Contractor Assessment · PoC", "file": "contractor-assessment-poc.html"},
        {"name": "WASH · Maturity Framework",   "file": "wash_maturity_framework_fr.html"},
        {"name": "Groundwater data",            "file": "groundwater_connector.html"},
    ],
    "Internal tools": [
        {"name": "ASWA3 baseline dashboard",     "file": "PoC3-ASWA3baseline.html"},
        {"name": "Country Opportunity",          "file": "wash_explorer_map_v3.html"},
        {"name": "Data for WASH · Concept",      "file": "data_for_wash_complete_v4_1.html"},
        {"name": "Akvo · Theory of Change",      "file": "akvo_toc_with_assumptions.html"},
        {"name": "Why Akvo's Work Matters in WASH Data", "file": "akvo_mindmap_v3_html.html"},
        {"name": "Investment in Data Infrastructure", "url": "https://claude.ai/public/artifacts/8af6253a-5894-4e26-85e5-45d361d1eea0"},
    ],
}

ALL_PAGES = {p["name"]: p for section in SECTIONS.values() for p in section}

if "selected_page" not in st.session_state:
    default_page = SECTIONS["PoC"][0]["name"]
    requested = st.query_params.get("page", None)
    if requested:
        requested_lower = requested.lower()
        for name in ALL_PAGES:
            if requested_lower in name.lower():
                default_page = name
                break
    st.session_state.selected_page = default_page

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700&family=Roboto+Condensed:wght@700&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"] {
        font-family: 'Assistant', system-ui, sans-serif;
    }
    /* Remove all top padding from main content area */
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
    [data-testid="stMainBlockContainer"] {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
    /* Hide Streamlit's header bar and rainbow decoration */
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stDecoration"] { display: none !important; }
    /* Remove gap above iframe */
    [data-testid="stVerticalBlockBorderWrapper"] { padding: 0 !important; }
    iframe { display: block; }
    section[data-testid="stSidebar"] > div {
        padding-top: 0 !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #f8faf9;
        border-right: 1px solid #e0ebe7;
    }
    div[data-testid="stSidebar"] .stButton > button {
        width: 100%;
        text-align: left;
        background: transparent;
        border: none;
        border-radius: 6px;
        padding: 8px 14px;
        font-family: 'Assistant', sans-serif;
        font-size: 14px;
        font-weight: 500;
        color: #3a3a3a;
        cursor: pointer;
        transition: background 0.15s, color 0.15s;
        white-space: normal;
        line-height: 1.4;
    }
    div[data-testid="stSidebar"] .stButton > button:hover {
        background-color: #e0f7f3;
        color: #027a64;
    }
    div[data-testid="stSidebar"] .stButton > button:focus {
        box-shadow: none;
    }
    div[data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background-color: #03AD8C !important;
        color: #ffffff !important;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

def section_label(title):
    st.markdown(f"""
    <div style="font-family:'Roboto Condensed',sans-serif; font-size:10px; font-weight:700;
                letter-spacing:0.1em; text-transform:uppercase; color:#9ab0aa;
                padding: 16px 14px 6px 14px;">
        {title}
    </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.image("akvo_logo.png", width=120)
    st.markdown("""
    <div style="padding: 4px 16px 16px 16px;">
        <div style="font-family:'Assistant',sans-serif; font-size:13px; color:#6b7c76;
                    margin-bottom:16px;">Water project PoC</div>
        <div style="height:2px; background:#03AD8C; border-radius:2px;"></div>
    </div>
    """, unsafe_allow_html=True)

    for section_title, pages in SECTIONS.items():
        section_label(section_title)
        for page in pages:
            is_active = st.session_state.selected_page == page["name"]
            if st.button(page["name"], key=page["name"], type="primary" if is_active else "secondary"):
                st.session_state.selected_page = page["name"]
                st.rerun()

    st.markdown("""
    <div style="padding: 24px 16px 16px 16px; margin-top: 8px;
                border-top: 1px solid #e0ebe7;">
        <span style="font-family:'Assistant',sans-serif; font-size:11px; color:#9ab0aa;">
            akvo.org
        </span>
    </div>
    """, unsafe_allow_html=True)

# ── Main area ──────────────────────────────────────────────────────────────────
selection = st.session_state.selected_page
page = ALL_PAGES[selection]

if "url" in page:
    url = page["url"]
    st.markdown(f"""
    <div style="font-family:'Assistant',sans-serif; padding: 32px 0 16px 0;">
        <div style="font-size:22px; font-weight:700; color:#202024; margin-bottom:8px;">{selection}</div>
        <div style="font-size:14px; color:#6b7c76; margin-bottom:24px;">This project is hosted externally.</div>
        <a href="{url}" target="_blank" style="text-decoration:none;">
            <button style="background:#03AD8C; color:#fff; padding:11px 24px; border:none;
                           border-radius:8px; font-family:'Assistant',sans-serif; font-size:15px;
                           font-weight:600; cursor:pointer;">↗ Open in new tab</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

else:
    html_file = page["file"]
    if not os.path.exists(html_file):
        st.error(f"File not found: **{html_file}**")
    else:
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()
        # Inject a script that resizes the Streamlit iframe to fit the viewport
        resize_script = """
<script>
(function() {
  function setHeight() {
    var h = window.innerHeight || document.documentElement.clientHeight || 900;
    // Tell the parent Streamlit frame to resize this iframe
    window.parent.postMessage({isStreamlitMessage: true, type: 'streamlit:setFrameHeight', height: h}, '*');
  }
  setHeight();
  window.addEventListener('resize', setHeight);
})();
</script>"""
        html_with_resize = html_content.replace('</body>', resize_script + '\n</body>')
        st.components.v1.html(html_with_resize, height=1100, scrolling=True)
