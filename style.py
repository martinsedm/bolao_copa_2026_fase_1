# style.py - removendo acentuacoes (mantendo apenas CSS)
import streamlit as st

CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700&display=swap');

  :root {
    --green:  #009C3B;
    --yellow: #FFDF00;
    --blue:   #002776;
    --white:  #FFFFFF;
    --gray50: #F8F9FA;
    --gray100:#F1F3F5;
    --gray300:#DEE2E6;
    --gray600:#6C757D;
    --gray900:#212529;
    --gold:   #FFB800;
    --silver: #A0A0A0;
    --bronze: #CD7F32;
  }

  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

  /* Header strip */
  .bolao-header {
    background: linear-gradient(135deg, var(--blue) 0%, #003a99 100%);
    color: var(--white);
    padding: 1.4rem 2rem 1.2rem;
    border-radius: 12px;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    border-bottom: 4px solid var(--yellow);
  }
  .bolao-header h1 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.6rem;
    letter-spacing: 2px;
    margin: 0;
    color: var(--yellow);
    line-height: 1;
  }
  .bolao-header p { margin: 0; font-size: .85rem; opacity: .8; }

  /* Tab styling */
  .stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: var(--gray100);
    padding: 6px;
    border-radius: 10px;
  }
  .stTabs [data-baseweb="tab"] {
    padding: 8px 22px;
    border-radius: 8px;
    font-weight: 600;
    font-size: .9rem;
    color: var(--gray600);
  }
  .stTabs [aria-selected="true"] {
    background: var(--blue) !important;
    color: var(--white) !important;
  }

  /* Ranking table */
  .rank-table { width: 100%; border-collapse: collapse; }
  .rank-table th {
    background: var(--blue);
    color: var(--yellow);
    font-size: .75rem;
    text-transform: uppercase;
    letter-spacing: .5px;
    padding: 10px 12px;
    text-align: center;
  }
  .rank-table th:first-child { text-align: left; border-radius: 0; }
  .rank-table td {
    padding: 9px 12px;
    font-size: .9rem;
    border-bottom: 1px solid var(--gray100);
    text-align: center;
    color: var(--gray900);
  }
  .rank-table td:nth-child(2) { text-align: left; font-weight: 600; }
  .rank-table tr:hover td { background: var(--gray50); }
  .rank-table tr.top3 td { font-weight: 700; }
  .posicao { 
    font-weight: 700; 
    font-size: 1rem;
    color: var(--gray900);
  }
  .pts-badge {
    display: inline-block;
    background: var(--blue);
    color: var(--yellow);
    border-radius: 20px;
    padding: 2px 10px;
    font-weight: 700;
    font-size: .95rem;
  }

  /* Game cards */
  .game-card {
    background: var(--white);
    border: 1px solid var(--gray300);
    border-radius: 10px;
    padding: 12px 16px;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: box-shadow .15s;
  }
  .game-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,.1); }
  .game-card.has-result { border-left: 4px solid var(--green); }
  .game-card.is-brasil { border-left: 4px solid var(--yellow); background: #fffef0; }
  .team-name { font-weight: 600; font-size: .9rem; flex: 1; text-align: center; }
  .score-box {
    background: var(--gray100);
    border-radius: 6px;
    padding: 4px 12px;
    font-weight: 700;
    font-size: 1rem;
    color: var(--blue);
    min-width: 60px;
    text-align: center;
  }
  .score-box.final { background: var(--blue); color: var(--yellow); }
  .day-badge {
    background: var(--gray100);
    color: var(--gray600);
    font-size: .72rem;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 4px;
    white-space: nowrap;
  }

  /* Admin form */
  .admin-section {
    background: var(--gray50);
    border: 1px solid var(--gray300);
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 10px;
  }

  /* Bet detail */
  .bet-row {
    display: flex;
    align-items: center;
    padding: 5px 0;
    border-bottom: 1px solid var(--gray100);
    font-size: .88rem;
  }
  .bet-row:last-child { border-bottom: none; }
  .bet-name { width: 110px; font-weight: 600; color: var(--gray900); }
  .bet-score { width: 60px; text-align: center; color: var(--blue); font-weight: 700; }
  .pts-chip {
    border-radius: 12px;
    padding: 1px 8px;
    font-size: .78rem;
    font-weight: 700;
    margin-left: 6px;
  }
  .pts-6 { background: #198754; color: #fff; }
  .pts-4 { background: #0d6efd; color: #fff; }
  .pts-3 { background: #fd7e14; color: #fff; }
  .pts-1 { background: #adb5bd; color: #fff; }
  .pts-0 { background: #f8d7da; color: #842029; }

  /* Progress bar */
  .progress-wrap { background: var(--gray100); border-radius: 4px; height: 8px; margin-top: 4px; }
  .progress-fill { height: 8px; border-radius: 4px; background: var(--green); }

  /* Stats cards */
  .stat-card {
    background: linear-gradient(135deg, var(--blue), #003a99);
    color: var(--white);
    border-radius: 10px;
    padding: 16px 20px;
    text-align: center;
  }
  .stat-card .stat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.4rem;
    color: var(--yellow);
    line-height: 1;
  }
  .stat-card .stat-lbl { font-size: .78rem; opacity: .8; text-transform: uppercase; letter-spacing: .5px; margin-top: 2px; }

  /* Streamlit overrides */
  div[data-testid="stVerticalBlock"] > div { gap: 0 !important; }
  .block-container { padding-top: 1rem !important; }
  footer { visibility: hidden; }
  .stAlert { border-radius: 8px; }

  /* Hide Streamlit's default multipage nav in sidebar */
  [data-testid="stSidebarNav"] { display: none; }

  /* Sticky header for tables */
  .sticky-table-container {
    max-height: 600px;
    overflow-y: auto;
    overflow-x: auto;
    position: relative;
  }
  
  .sticky-table-container table {
    width: 100%;
    border-collapse: collapse;
    font-size: .85rem;
  }
  
  .sticky-table-container thead th {
    position: sticky;
    top: 0;
    background: var(--blue);
    color: var(--yellow);
    font-size: .75rem;
    text-transform: uppercase;
    letter-spacing: .5px;
    padding: 10px 8px;
    text-align: center;
    z-index: 10;
    white-space: nowrap;
    border-bottom: 2px solid var(--yellow);
  }
  
  .sticky-table-container thead th:first-child {
    text-align: center;
  }
  
  .sticky-table-container thead th:nth-child(2) {
    text-align: left;
  }
  
  .sticky-table-container tbody td {
    padding: 8px 6px;
    border-bottom: 1px solid var(--gray100);
    text-align: center;
    color: var(--gray900);
    white-space: nowrap;
  }
  
  .sticky-table-container tbody td:nth-child(2) {
    text-align: left;
    font-weight: 500;
    white-space: nowrap;
  }
  
  .sticky-table-container tbody tr:hover td {
    background: var(--gray50);
  }
  
  /* Shadow effect when scrolling */
  .sticky-table-container::after {
    content: '';
    position: sticky;
    bottom: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(to bottom, transparent, rgba(0,0,0,0.05));
    pointer-events: none;
    display: block;
  }
</style>
"""

HEADER = """
<div class="bolao-header">
  <div style="font-size:2.8rem">:soccer:</div>
  <div>
    <h1>BOLAO COPA 2026</h1>
    <p>Confraternizacao · 1a Fase · 72 Jogos</p>
  </div>
</div>
"""


def inject_style():
    st.markdown(CSS, unsafe_allow_html=True)


def show_header():
    st.markdown(HEADER, unsafe_allow_html=True)