# app.py - removendo acentuações
import streamlit as st
from data import load_data, compute_standings, PARTICIPANTS, calc_points
from style import inject_style, show_header

st.set_page_config(
    page_title="Bolao Copa 2026",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_style()
show_header()

data = load_data()

scoring = data.get("scoring", {
    "exact_score": 6,
    "one_goal_and_winner": 4,
    "winner_and_one_goal": 3,
    "winner_only": 1
})
# ── Tabs ─────────────────────────────────────────────────────────────────────
tab_rank, tab_jogos, tab_palpites = st.tabs([":trophy:  Classificacao", ":soccer:  Jogos", ":clipboard:  Palpites"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 – CLASSIFICACAO
# ══════════════════════════════════════════════════════════════════════════════
with tab_rank:
    standings = compute_standings(data)
    total_games = len(data["games"])
    played = sum(1 for g in data["games"] if g["result_g1"] is not None)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="stat-card"><div class="stat-num">{played}</div><div class="stat-lbl">Jogos com resultado</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-card"><div class="stat-num">{total_games - played}</div><div class="stat-lbl">Jogos restantes</div></div>', unsafe_allow_html=True)
    with c3:
        leader_pts = standings[0]["total"] if standings else 0
        st.markdown(f'<div class="stat-card"><div class="stat-num">{leader_pts}</div><div class="stat-lbl">Pontos do lider</div></div>', unsafe_allow_html=True)
    with c4:
        pct = int(played / total_games * 100) if total_games else 0
        st.markdown(f'<div class="stat-card"><div class="stat-num">{pct}%</div><div class="stat-lbl">Progresso</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    rows = ""
    current_rank = None
    rank_has_been_shown = False
    
    for i, s in enumerate(standings):
        # Verifica se e um novo grupo de posicao
        if s["rank"] != current_rank:
            current_rank = s["rank"]
            rank_has_been_shown = False
        
        # Mostra a posicao apenas se ainda nao foi mostrada para este grupo
        if not rank_has_been_shown:
            posicao = f"{s['rank']}o"
            rank_has_been_shown = True
        else:
            posicao = ""  # Nao mostra posicao para participantes empatados
        
        top_cls = "top3" if s["rank"] <= 3 else ""
        pts_html = f'<span class="pts-badge">{s["total"]}</span>'
        
        # Adiciona um indicador visual para os empatados
        if posicao == "":
            rows += (
                f'<tr class="{top_cls}">'
                f'<td><span class="posicao" style="color:#6c757d;">↳</span></td>'
                f'<td style="padding-left: 20px;">{s["name"]}</td>'
                f'<td>{pts_html}</td>'
                f'<td>{s["pts6"]}</td>'
                f'<td>{s["pts4"]}</td>'
                f'<td>{s["pts3"]}</td>'
                f'<td>{s["pts1"]}</td>'
                f'<td>{s["brasil"]}</td>'
                f'</tr>'
            )
        else:
            rows += (
                f'<tr class="{top_cls}">'
                f'<td><span class="posicao">{posicao}</span></td>'
                f'<td>{s["name"]}</td>'
                f'<td>{pts_html}</td>'
                f'<td>{s["pts6"]}</td>'
                f'<td>{s["pts4"]}</td>'
                f'<td>{s["pts3"]}</td>'
                f'<td>{s["pts1"]}</td>'
                f'<td>{s["brasil"]}</td>'
                f'</tr>'
            )

    table_html = (
        '<table class="rank-table">'
        '<thead><tr>'
        '<th>#</th>'
        '<th style="text-align:left">Participante</th>'
        '<th>Total</th>'
        '<th>6pts</th>'
        '<th>4pts</th>'
        '<th>3pts</th>'
        '<th>1pt</th>'
        '<th>Brasil</th>'
        '</tr></thead>'
        f'<tbody>{rows}</tbody>'
        '</table>'
        '<br>'
        '<small style="color: #6c757d;">'
        ':star: Placar exato (6 pts) &nbsp;|&nbsp; :dart: Um gol + vencedor (4 pts) &nbsp;|&nbsp; '
        ':white_check_mark: Vencedor + um gol (3 pts) &nbsp;|&nbsp; :thumbsup: So vencedor (1 pt) &nbsp;|&nbsp; '
        ':brazil: Pontos em jogos do Brasil (desempate)'
        '</small>'
    )
    st.markdown(table_html, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 – JOGOS
# ══════════════════════════════════════════════════════════════════════════════
with tab_jogos:
    col_f1, col_f2 = st.columns([1, 2])
    with col_f1:
        filter_status = st.selectbox(
            "Filtrar por status",
            ["Todos", "Com resultado", "Sem resultado", "Jogos do Brasil"],
            label_visibility="collapsed",
            key="filter_status_jogos"
        )
    with col_f2:
        search = st.text_input(
            "Buscar time...", 
            placeholder="Ex: Brasil, Argentina", 
            label_visibility="collapsed",
            key="search_jogos"
        )

    days = {}
    for g in data["games"]:
        d = g["dia"]
        days.setdefault(d, []).append(g)

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

        st.markdown("---")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 – PALPITES
# ══════════════════════════════════════════════════════════════════════════════
with tab_palpites:
    st.markdown("Veja os palpites de cada participante e a pontuacao obtida ate agora.")
    
    # Opcao para escolher entre visualizacao individual ou todos os participantes
    view_mode = st.radio(
        "Modo de visualizacao",
        ["Participante individual", "Todos os participantes"],
        horizontal=True,
        key="view_mode"
    )
    
    if view_mode == "Participante individual":
        # Modo individual (ja existente)
        col_p, col_g = st.columns([1, 2])
        with col_p:
            selected_p = st.selectbox("Participante", PARTICIPANTS, key="selected_participant")
        with col_g:
            filter_g = st.selectbox(
                "Jogos",
                ["Todos os jogos", "Jogos com resultado", "Jogos sem resultado", "Jogos do Brasil"],
                label_visibility="collapsed",
                key="filter_g_individual"
            )

        total_pts = 0
        rows_html = ""

        for g in data["games"]:
            has_result = g["result_g1"] is not None
            if filter_g == "Jogos com resultado" and not has_result:
                continue
            if filter_g == "Jogos sem resultado" and has_result:
                continue
            if filter_g == "Jogos do Brasil" and not g["is_brasil"]:
                continue

            bet = g["bets"].get(selected_p, {})
            b1, b2 = bet.get("g1", "?"), bet.get("g2", "?")
            pts = calc_points(
                g["result_g1"],
                g["result_g2"],
                b1,
                b2,
                scoring
            ) if has_result else None
            total_pts += pts if pts else 0

            if has_result:
                result_str = f"{g['result_g1']} x {g['result_g2']}"
                pts_cls = f"pts-{pts}" if pts is not None else "pts-0"
                pts_lbl = f'<span class="pts-chip {pts_cls}">{pts} pt{"s" if pts != 1 else ""}</span>'
            else:
                result_str = "— x —"
                pts_lbl = '<span style="color:#aaa;font-size:.78rem">pendente</span>'

            brasil_icon = " :brazil:" if g["is_brasil"] else ""
            rows_html += (
                f'<div class="bet-row">'
                f'<span style="width:28px;color:#aaa;font-size:.78rem">{g["id"]+1}</span>'
                f'<span style="flex:1;font-size:.85rem">{g["pais1"]} x {g["pais2"]}{brasil_icon}</span>'
                f'<span class="bet-score">{b1} x {b2}</span>'
                f'<span style="width:70px;text-align:center;font-size:.8rem;color:#6c757d">{result_str}</span>'
                f'{pts_lbl}'
                f'</div>'
            )

        pct_done = int(sum(1 for g in data["games"] if g["result_g1"] is not None) / len(data["games"]) * 100)

        final_html = (
            f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:12px">'
            f'<div>'
            f'<div style="font-size:.8rem;color:#6c757d;text-transform:uppercase;letter-spacing:.5px">Total de pontos</div>'
            f'<div style="font-size:2rem;font-weight:700;color:#002776">{total_pts} pts</div>'
            f'</div>'
            f'<div style="flex:1">'
            f'<div style="font-size:.78rem;color:#6c757d">Progresso do torneio: {pct_done}%</div>'
            f'<div class="progress-wrap"><div class="progress-fill" style="width:{pct_done}%"></div></div>'
            f'</div>'
            f'</div>'
            f'<div style="background:#fff;border:1px solid #dee2e6;border-radius:10px;padding:12px 16px;overflow-x:auto">'
            f'<div style="display:flex;gap:10px;padding-bottom:8px;border-bottom:2px solid #f1f3f5;font-size:.75rem;font-weight:700;color:#6c757d;text-transform:uppercase;letter-spacing:.5px">'
            f'<span style="width:28px">#</span>'
            f'<span style="flex:1">Jogo</span>'
            f'<span style="width:60px;text-align:center">Palpite</span>'
            f'<span style="width:70px;text-align:center">Resultado</span>'
            f'<span style="width:60px;text-align:center">Pontos</span>'
            f'</div>'
            f'{rows_html if rows_html else "<div style=\'color:#aaa;text-align:center;padding:20px\'>Nenhum jogo encontrado.</div>"}'
            f'</div>'
        )
        st.markdown(final_html, unsafe_allow_html=True)
    
    else:
        # Modo "Todos os participantes"
        col_f1, col_f2 = st.columns([1, 2])
        with col_f1:
            filter_g = st.selectbox(
                "Jogos",
                ["Todos os jogos", "Jogos com resultado", "Jogos sem resultado", "Jogos do Brasil"],
                label_visibility="collapsed",
                key="filter_g_all"
            )
        with col_f2:
            search = st.text_input(
                "Buscar time...", 
                placeholder="Ex: Brasil, Argentina", 
                label_visibility="collapsed",
                key="search_all"
            )
        
        # Construir a tabela HTML
        table_rows = ""
        
        for g in data["games"]:
            has_result = g["result_g1"] is not None
            
            # Aplicar filtros
            if filter_g == "Jogos com resultado" and not has_result:
                continue
            if filter_g == "Jogos sem resultado" and has_result:
                continue
            if filter_g == "Jogos do Brasil" and not g["is_brasil"]:
                continue
            if search and search.lower() not in g["pais1"].lower() and search.lower() not in g["pais2"].lower():
                continue
        
            # Numero do jogo
            row = f'<tr><td style="text-align:center;font-weight:600;color:#6c757d">{g["id"]+1}</td>'
        
            # Nome do jogo
            brasil_icon = " :brazil:" if g["is_brasil"] else ""
            row += f'<td style="font-weight:500;white-space:nowrap">{g["pais1"]} x {g["pais2"]}{brasil_icon}</td>'
          
            # Palpites de cada participante
            for p in PARTICIPANTS:
                bet = g["bets"].get(p, {})
                b1, b2 = bet.get("g1", "?"), bet.get("g2", "?")
            
                if has_result:
                    pts = calc_points(g["result_g1"], g["result_g2"], b1, b2, scoring)
                    pts_text = f'{b1}x{b2} <span style="font-size:.7rem;color:#6c757d">({pts}pts)</span>'
                else:
                    pts_text = f'{b1}x{b2}'
            
                row += f'<td style="text-align:center;font-size:.85rem;white-space:nowrap">{pts_text}</td>'
        
            # Resultado
            if has_result:
                result_text = f'<span style="font-weight:700;color:#002776">{g["result_g1"]}x{g["result_g2"]}</span>'
            else:
                result_text = '<span style="color:#aaa">—x—</span>'
            row += f'<td style="text-align:center;font-weight:600;white-space:nowrap">{result_text}</td></tr>'
        
            table_rows += row
    
        # Construir cabecalho da tabela
        thead = '<thead><tr><th style="text-align:center;min-width:30px">#</th><th style="text-align:left;min-width:120px">Jogo</th>'
        for p in PARTICIPANTS:
            # Nome do participante com cor especial para o Brasil
            if p == "Brasil":
                thead += f'<th style="text-align:center;background:#FFDF00;color:#002776;min-width:70px">{p}</th>'
            else:
                thead += f'<th style="text-align:center;min-width:70px">{p}</th>'
        thead += '<th style="text-align:center;min-width:70px">Resultado</th></tr></thead>'
      
        # Montar tabela completa com container para scroll
        if table_rows:
            table_html = (
                f'<div style="background:#fff;border:1px solid #dee2e6;border-radius:10px;padding:8px;overflow-x:auto">'
                f'<div class="sticky-table-container">'
                f'<table>'
                f'{thead}'
                f'<tbody>{table_rows}</tbody>'
                f'</table>'
                f'</div>'
                f'</div>'
            )
        else:
            table_html = '<div style="color:#aaa;text-align:center;padding:40px">Nenhum jogo encontrado com os filtros selecionados.</div>'
    
        st.markdown(table_html, unsafe_allow_html=True)
    
        # Legenda
        st.markdown(
            '<small style="color: #6c757d;">'
            ':bar_chart: Cada celula mostra o palpite (Gols1xGols2) e entre parenteses a pontuacao obtida no jogo (apenas para jogos com resultado). '
            'O cabecalho da tabela permanece fixo durante a rolagem.'
            '</small>',
            unsafe_allow_html=True
        )