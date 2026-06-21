# admin.py - removendo acentuações
import streamlit as st
from data import load_data, save_data
from style import inject_style, show_header
from data import atualizar_todos_os_pontos

st.set_page_config(
    page_title="Admin · Bolao Copa 2026",
    page_icon=":lock:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_style()

# ── Password gate ────────────────────────────────────────────────────────────
if "admin_ok" not in st.session_state:
    st.session_state.admin_ok = False

if not st.session_state.admin_ok:
    show_header()
    st.markdown("### :lock: Area restrita")
    pwd = st.text_input("Senha de administrador", type="password")
    if st.button("Entrar", type="primary"):
        if pwd == "VemHexa2026":
            st.session_state.admin_ok = True
            st.rerun()
        else:
            st.error("Senha incorreta.")
    st.stop()

# ── Admin content ────────────────────────────────────────────────────────────
show_header()
st.markdown("## :key: Administracao — Resultados dos Jogos")

col_logout, _ = st.columns([1, 5])
with col_logout:
    if st.button(":door: Sair"):
        st.session_state.admin_ok = False
        st.rerun()

data = load_data()

col_f1, col_f2 = st.columns([1, 2])
with col_f1:
    filter_status = st.selectbox(
        "Filtrar por status",
        ["Todos", "Com resultado", "Sem resultado", "Jogos do Brasil"],
        label_visibility="collapsed"
    )
with col_f2:
    search = st.text_input("Buscar time...", placeholder="Ex: Brasil, Argentina", label_visibility="collapsed")

days = {}
for g in data["games"]:
    days.setdefault(g["dia"], []).append(g)

for day in sorted(days.keys()):
    games_in_day = days[day]

    filtered = []
    for g in games_in_day:
        if filter_status == "Com resultado" and g["result_g1"] is None:
            continue
        if filter_status == "Sem resultado" and g["result_g1"] is not None:
            continue
        if filter_status == "Jogos do Brasil" and not g["is_brasil"]:
            continue
        if search and search.lower() not in g["pais1"].lower() and search.lower() not in g["pais2"].lower():
            continue
        filtered.append(g)

    if not filtered:
        continue

    st.markdown(f"**:calendar: Dia {day} de junho**")

    for g in filtered:
        has_result = g["result_g1"] is not None
        is_brasil = g["is_brasil"]
        cls = "is-brasil" if is_brasil else ("has-result" if has_result else "")

        if has_result:
            score_html = f'<div class="score-box final">{g["result_g1"]} x {g["result_g2"]}</div>'
        else:
            score_html = '<div class="score-box">— x —</div>'

        brasil_flag = " :brazil:" if is_brasil else ""
        status_html = (
            "<small style='color:#198754;font-size:.75rem'>✓ resultado registrado</small>"
            if has_result else
            "<small style='color:#aaa;font-size:.75rem'>aguardando</small>"
        )
        card_html = (
            f'<div class="game-card {cls}">'
            f'<span class="day-badge">Jogo {g["id"]+1}</span>'
            f'<span class="team-name">{g["pais1"]}{brasil_flag if g["pais1"]=="Brasil" else ""}</span>'
            f'{score_html}'
            f'<span class="team-name">{g["pais2"]}{brasil_flag if g["pais2"]=="Brasil" else ""}</span>'
            f'{status_html}'
            f'</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)

        with st.expander(f"{':pencil: Editar resultado' if has_result else ':heavy_plus_sign: Registrar resultado'}: {g['pais1']} x {g['pais2']}", expanded=False):
            ca, cb, cc = st.columns([2, 1, 2])
            with ca:
                g1 = st.number_input(
                    g["pais1"], min_value=0, max_value=20,
                    value=int(g["result_g1"]) if has_result else 0,
                    key=f"g1_{g['id']}"
                )
            with cb:
                st.markdown("<br><div style='text-align:center;font-size:1.2rem;font-weight:700'>x</div>", unsafe_allow_html=True)
            with cc:
                g2 = st.number_input(
                    g["pais2"], min_value=0, max_value=20,
                    value=int(g["result_g2"]) if has_result else 0,
                    key=f"g2_{g['id']}"
                )
            col_save, col_del = st.columns([1, 1])
            with col_save:
                if st.button(":floppy_disk: Salvar", key=f"save_{g['id']}", type="primary", use_container_width=True):
                    data["games"][g["id"]]["result_g1"] = g1
                    data["games"][g["id"]]["result_g2"] = g2
                    atualizar_todos_os_pontos(data)
                    save_data(data)
                    st.success(f"Resultado salvo: {g['pais1']} {g1} x {g2} {g['pais2']}")
                    st.rerun()
            with col_del:
                if has_result:
                    if st.button(":wastebasket: Limpar", key=f"del_{g['id']}", use_container_width=True):
                        data["games"][g["id"]]["result_g1"] = None
                        data["games"][g["id"]]["result_g2"] = None
                        atualizar_todos_os_pontos(data)
                        save_data(data)
                        st.warning("Resultado removido")
                        st.rerun()

    st.markdown("---")