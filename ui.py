"""Direction artistique commune de PASSIR Calculateur."""
import streamlit as st


def injecter_style() -> None:
    st.markdown("""
    <style>
      :root {
        --passir-ink: #132c22; --passir-green: #17683d; --passir-green-deep: #0d2b20;
        --passir-orange: #bb5200; --passir-orange-soft: #fff0e2; --passir-cream: #f7f7f2;
        --passir-paper: #ffffff; --passir-line: #d9e2da; --passir-muted: #52665b;
      }
      .stApp { background: var(--passir-cream); color: var(--passir-ink); font-family: Aptos, "Segoe UI", Inter, Arial, sans-serif; }
      .block-container { max-width: 1240px; padding-top: 2.15rem; padding-bottom: 3.5rem; }
      [data-testid="stHeader"] { background: rgba(247, 247, 242, .94); border-bottom: 1px solid rgba(19, 44, 34, .06); }
      [data-testid="stDeployButton"] { display: none !important; }
      .st-key-navigation { position: fixed; top: .55rem; right: 1.2rem; width: 145px; z-index: 999990; }
      .st-key-navigation button { background: #fff !important; color: #132c22 !important; border: 1px solid #b9c8bd !important; }
      [data-testid="stToolbar"] { margin-right: 160px; }
      [data-testid="collapsedControl"], [data-testid="stSidebarCollapsedControl"] { visibility: visible !important; opacity: 1 !important; z-index: 999991; }
      .brand-line { display:flex; align-items:center; gap:12px; margin: .7rem 0 1.1rem; }
      .brand-mark { width:38px; height:38px; border-radius:12px; background:#143d2a; color:#f6bd74; display:grid; place-items:center; font-family:Georgia,serif; font-size:24px; }
      .brand-title { font-size:1.1rem; font-weight:800; letter-spacing:.12em; color:#143d2a; }
      .brand-subtitle { font-size:.76rem; color:#52665b; }
      .result-reveal { padding:1rem 1.2rem; border-left:4px solid #bb5200; background:#edf3eb; border-radius:12px; animation: reveal .55s ease-out; margin-bottom:1rem; }
      @keyframes reveal { from { opacity:0; transform:translateY(14px); } to { opacity:1; transform:translateY(0); } }
      @media (prefers-reduced-motion: reduce) { .result-reveal { animation:none; } }
      [data-testid="stSidebar"] { background: var(--passir-green-deep); border-right: 1px solid rgba(255,255,255,.10); }
      [data-testid="stSidebar"] * { color: #f7f7f2 !important; }
      [data-testid="stSidebarNav"] a { border-radius: 9px; margin: .14rem .45rem; padding: .65rem .75rem; opacity: .85; }
      [data-testid="stSidebarNav"] a:hover, [data-testid="stSidebarNav"] a[aria-current="page"] { background: rgba(255,255,255,.13); opacity: 1; }
      [data-testid="stSidebarCollapseButton"] button { color: #f7f7f2 !important; background: rgba(255,255,255,.12) !important; border-radius: 8px !important; }
      [data-testid="stSidebarCollapsedControl"] { display: flex !important; opacity: 1 !important; background: #fff !important; border: 1px solid var(--passir-line) !important; border-radius: 0 10px 10px 0 !important; box-shadow: 0 7px 18px rgba(13,43,32,.16); }
      [data-testid="stSidebarCollapsedControl"] button { min-width: 5.5rem !important; min-height: 2.6rem !important; color: var(--passir-green-deep) !important; background: #fff !important; border: 0 !important; font-weight: 800 !important; }
      [data-testid="stSidebarCollapsedControl"] button::after { content: "Menu"; margin-left: .3rem; font-family: Aptos, "Segoe UI", sans-serif; font-size: .78rem; }
      h1, h2, h3 { color: var(--passir-ink) !important; font-family: Georgia, "Times New Roman", serif; font-weight: 700 !important; letter-spacing: -.026em; }
      h1 { font-size: clamp(2.05rem, 4vw, 3.1rem) !important; line-height: 1.05 !important; margin-bottom: .55rem !important; }
      h2 { margin-top: 2rem !important; } h3 { font-size: 1.18rem !important; }
      p, li, [data-testid="stCaptionContainer"] { color: var(--passir-muted); line-height: 1.65; }
      .hero { position: relative; overflow: hidden; isolation: isolate; background: linear-gradient(128deg, #0d2b20 0%, #155c37 100%); color: #fff; border-radius: 22px; padding: clamp(2rem, 5vw, 4.25rem); margin: .35rem 0 2.25rem; box-shadow: 0 18px 42px rgba(13, 43, 32, .16); }
      .hero::before { content: ""; position: absolute; z-index: -1; width: 24rem; height: 24rem; right: -8rem; top: -11rem; border-radius: 50%; background: #d86b13; opacity: .95; }
      .hero::after { content: ""; position: absolute; z-index: -1; width: 13rem; height: 13rem; right: 4rem; bottom: -7rem; border: 1px solid rgba(255,255,255,.28); border-radius: 50%; }
      .hero .eyebrow { color: #f8c58a; font-family: Aptos, "Segoe UI", sans-serif; font-size: .75rem; font-weight: 750; letter-spacing: .15em; text-transform: uppercase; }
      .hero h1, .hero p { color: #fff !important; max-width: 45rem; margin-left: 0; } .hero h1 { margin-top: .5rem; } .hero p { opacity: .91; font-size: 1.06rem; margin-top: .85rem; }
      .page-kicker { color: var(--passir-orange); font-size: .76rem; font-weight: 800; letter-spacing: .13em; text-transform: uppercase; margin-bottom: .35rem; }
      .workflow-card { min-height: 9.5rem; height: 100%; box-sizing: border-box; background: var(--passir-paper); border: 1px solid var(--passir-line); border-radius: 16px; padding: 1.2rem 1.35rem; box-shadow: 0 8px 20px rgba(19,44,34,.045); transition: transform .18s ease, box-shadow .18s ease; }
      .workflow-card:hover { transform: translateY(-3px); box-shadow: 0 14px 28px rgba(19,44,34,.10); }
      .workflow-index { color: var(--passir-orange); font-size: .78rem; font-weight: 800; letter-spacing: .12em; }
      .workflow-card h3 { margin: .5rem 0 .55rem !important; } .workflow-card p { margin: 0; font-size: .95rem; }
      .note { color: #4b2b10; border: 1px solid #e7bb87; border-left: 5px solid var(--passir-orange); background: var(--passir-orange-soft); padding: 1rem 1.15rem; border-radius: 10px; line-height: 1.55; }
      .muted { color: var(--passir-muted); font-size: .9rem; margin-top: 2.4rem; }
      [data-testid="stMetric"] { background: var(--passir-paper); border: 1px solid var(--passir-line); border-radius: 14px; padding: 1rem 1.1rem; box-shadow: 0 7px 18px rgba(19,44,34,.045); }
      [data-testid="stMetricLabel"] { color: var(--passir-muted); font-weight: 650; }
      [data-testid="stMetricValue"] { color: var(--passir-green-deep); font-family: Georgia, "Times New Roman", serif; font-weight: 700; }
      [data-testid="stExpander"] { background: var(--passir-paper); border: 1px solid var(--passir-line); border-radius: 12px; overflow: hidden; }
      [data-testid="stExpander"] details summary { background: #fff !important; padding: .72rem .85rem !important; }
      [data-testid="stExpander"] summary, [data-testid="stExpander"] summary p, [data-testid="stExpander"] summary span { color: var(--passir-ink) !important; font-weight: 750 !important; }
      [data-testid="stDataFrame"] { border: 1px solid var(--passir-line); border-radius: 11px; overflow: hidden; }
      [data-testid="stAlert"] { border-radius: 10px; }
      [data-testid="stNumberInput"] input, [data-testid="stSelectbox"] [data-baseweb="select"] > div { background: #fff !important; border-color: #b9c8bd !important; color: var(--passir-ink) !important; border-radius: 9px !important; }
      [data-testid="stNumberInput"] input:focus, [data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within { border-color: var(--passir-green) !important; box-shadow: 0 0 0 3px rgba(23,104,61,.14) !important; }
      [data-testid="stButton"] > button, [data-testid="stDownloadButton"] > button { border-radius: 9px; font-weight: 750; letter-spacing: .005em; min-height: 2.65rem; transition: transform .16s ease, box-shadow .16s ease, background .16s ease; }
      button[data-testid="stBaseButton-primary"], [data-testid="stButton"] > button[kind="primary"], [data-testid="stDownloadButton"] > button { background: var(--passir-orange) !important; color: #fff !important; border: 1px solid var(--passir-orange) !important; box-shadow: 0 6px 14px rgba(187,82,0,.16); }
      button[data-testid="stBaseButton-primary"] *, [data-testid="stButton"] > button[kind="primary"] *, [data-testid="stDownloadButton"] > button * { color: #fff !important; }
      [data-testid="stButton"] > button[kind="secondary"] { background: var(--passir-paper); color: var(--passir-green-deep); border: 1px solid #aebfb2; }
      [data-testid="stButton"] > button:hover, [data-testid="stDownloadButton"] > button:hover { transform: translateY(-1px); filter: brightness(.94); }
      [data-testid="stButton"] > button:focus-visible, [data-testid="stDownloadButton"] > button:focus-visible { outline: 3px solid rgba(23,104,61,.3); outline-offset: 2px; }
      hr { border-color: var(--passir-line); margin: 2.1rem 0 !important; }
      @media (max-width: 700px) { .block-container { padding: 1.2rem 1rem 2rem; } .hero { border-radius: 16px; } }
    </style>
    """, unsafe_allow_html=True)

    with st.container(key="navigation"):
        with st.popover("☰ Menu", use_container_width=True):
            st.page_link("accueil.py", label="Accueil", icon="🏡")
            st.page_link("views/1_Calculateur.py", label="Simulation", icon="🌱")
            st.page_link("views/2_Fiche_du_projet.py", label="Le projet", icon="📖")
            st.page_link("views/3_Parametres.py", label="Paramètres", icon="⚙️")
