import json
import os
from pathlib import Path

DATA_FILE = Path(__file__).parent / "bolao_data.json"

PARTICIPANTS = [
    "Edmilson", "Cesare", "Daiane", "Julio", "Edvaldo",
    "Stella", "Caravelas", "Regis", "Kardec", "Fatima",
    "Laurita", "Edson", "Alessandra", "Marcelo"
]

BRASIL_TEAMS = {"Brasil"}

GAMES_RAW = [
    (11, "México", "África do Sul"),
    (11, "Coreia do Sul", "República Tcheca"),
    (12, "Canadá", "Bósnia-Herzegovina"),
    (12, "Estados Unidos", "Paraguai"),
    (14, "Austrália", "Turquia"),
    (13, "Qatar", "Suíça"),
    (13, "Brasil", "Marrocos"),
    (13, "Haiti", "Escócia"),
    (14, "Alemanha", "Curaçao"),
    (14, "Holanda", "Japão"),
    (14, "Costa do Marfim", "Equador"),
    (14, "Suécia", "Tunísia"),
    (15, "Espanha", "Cabo Verde"),
    (15, "Bélgica", "Egito"),
    (15, "Arábia Saudita", "Uruguai"),
    (15, "Irã", "Nova Zelândia"),
    (17, "Áustria", "Jordânia"),
    (16, "França", "Senegal"),
    (16, "Iraque", "Noruega"),
    (16, "Argentina", "Argélia"),
    (17, "Portugal", "Congo (RD)"),
    (17, "Inglaterra", "Croácia"),
    (17, "Gana", "Panamá"),
    (17, "Uzbequistão", "Colômbia"),
    (18, "República Tcheca", "África do Sul"),
    (18, "Suíça", "Bósnia-Herzegovina"),
    (18, "Canadá", "Qatar"),
    (18, "México", "Coreia do Sul"),
    (19, "Turquia", "Paraguai"),
    (19, "Estados Unidos", "Austrália"),
    (19, "Escócia", "Marrocos"),
    (19, "Brasil", "Haiti"),
    (20, "Tunísia", "Japão"),
    (20, "Holanda", "Suécia"),
    (20, "Alemanha", "Costa do Marfim"),
    (20, "Equador", "Curaçao"),
    (21, "Espanha", "Arábia Saudita"),
    (21, "Bélgica", "Irã"),
    (21, "Uruguai", "Cabo Verde"),
    (21, "Nova Zelândia", "Egito"),
    (23, "Jordânia", "Argélia"),
    (22, "Argentina", "Áustria"),
    (22, "França", "Iraque"),
    (22, "Noruega", "Senegal"),
    (23, "Portugal", "Uzbequistão"),
    (23, "Inglaterra", "Gana"),
    (23, "Panamá", "Croácia"),
    (23, "Colômbia", "Congo (RD)"),
    (24, "Suíça", "Canadá"),
    (24, "Bósnia-Herzegovina", "Qatar"),
    (24, "Escócia", "Brasil"),
    (24, "Marrocos", "Haiti"),
    (24, "República Tcheca", "México"),
    (24, "África do Sul", "Coreia do Sul"),
    (25, "Curaçao", "Costa do Marfim"),
    (25, "Equador", "Alemanha"),
    (25, "Japão", "Suécia"),
    (25, "Tunísia", "Holanda"),
    (25, "Turquia", "Estados Unidos"),
    (25, "Paraguai", "Austrália"),
    (26, "Noruega", "França"),
    (26, "Senegal", "Iraque"),
    (26, "Cabo Verde", "Arábia Saudita"),
    (26, "Uruguai", "Espanha"),
    (27, "Egito", "Irã"),
    (27, "Nova Zelândia", "Bélgica"),
    (27, "Panamá", "Inglaterra"),
    (27, "Croácia", "Gana"),
    (27, "Colômbia", "Portugal"),
    (27, "Congo (RD)", "Uzbequistão"),
    (27, "Argélia", "Áustria"),
    (27, "Jordânia", "Argentina"),
]

BETS_RAW = {
    "Edmilson": [(3,1),(1,1),(2,1),(1,2),(0,1),(0,2),(1,1),(0,1),(4,0),(3,2),(0,0),(2,1),(3,0),(1,0),(1,3),(1,0),(2,1),(4,1),(0,2),(2,0),(3,0),(2,1),(1,1),(0,1),(2,0),(2,1),(3,1),(1,1),(2,2),(1,0),(0,0),(3,0),(1,2),(1,0),(2,1),(3,0),(3,0),(2,0),(2,0),(0,2),(0,2),(1,0),(5,0),(1,1),(5,0),(3,1),(0,2),(2,0),(2,1),(2,1),(0,1),(4,0),(2,2),(0,1),(0,2),(0,2),(1,2),(1,2),(1,1),(2,0),(1,2),(2,0),(0,2),(1,2),(2,0),(0,2),(0,3),(2,1),(1,2),(1,0),(0,1),(0,2)],
    "Cesare": [(2,0),(1,2),(1,1),(0,1),(1,2),(0,2),(3,0),(1,1),(4,1),(2,1),(2,1),(1,0),(5,0),(3,0),(1,3),(1,0),(1,0),(3,1),(1,2),(2,0),(4,2),(1,0),(2,2),(1,3),(3,2),(2,2),(1,0),(2,1),(0,1),(3,1),(1,3),(4,2),(1,2),(1,0),(3,0),(2,0),(3,1),(3,0),(2,0),(0,2),(0,2),(1,0),(3,1),(1,1),(4,0),(3,1),(1,3),(2,0),(0,0),(1,0),(0,2),(3,1),(1,3),(0,2),(0,2),(0,2),(2,1),(1,3),(3,2),(2,1),(1,2),(0,0),(0,0),(2,3),(1,0),(0,4),(0,4),(1,0),(2,3),(0,0),(1,1),(1,5)],
    "Daiane": [(1,2),(0,0),(3,0),(0,4),(1,1),(3,2),(2,1),(2,0),(8,1),(1,0),(1,1),(1,1),(2,0),(3,2),(2,2),(2,2),(0,0),(4,2),(1,1),(3,2),(2,2),(3,2),(2,0),(1,2),(0,2),(1,1),(1,2),(3,2),(1,2),(0,3),(2,2),(4,0),(1,1),(2,1),(3,0),(2,0),(1,1),(2,4),(3,0),(0,3),(2,2),(5,3),(3,0),(2,3),(4,0),(3,2),(2,2),(3,1),(1,1),(1,3),(1,4),(1,2),(0,2),(5,2),(3,2),(2,6),(3,1),(1,5),(2,2),(4,2),(1,3),(3,2),(2,0),(3,2),(2,2),(1,3),(1,3),(0,2),(4,2),(3,3),(1,2),(0,6)],
    "Julio": [(1,1),(0,0),(0,0),(1,2),(0,1),(1,1),(2,1),(1,1),(3,0),(2,2),(2,0),(0,0),(3,0),(2,1),(1,3),(1,1),(0,0),(3,2),(0,0),(2,0),(2,0),(2,1),(2,1),(0,1),(0,2),(1,1),(1,1),(2,1),(0,3),(1,1),(0,2),(3,0),(0,3),(2,0),(3,1),(1,0),(2,0),(2,1),(2,0),(0,1),(0,0),(2,0),(3,0),(1,1),(2,0),(2,1),(0,1),(2,1),(1,1),(0,1),(0,3),(2,0),(0,2),(2,2),(0,1),(1,3),(3,1),(1,2),(0,1),(2,1),(0,4),(1,1),(0,1),(2,3),(1,1),(0,2),(0,2),(1,1),(1,2),(1,1),(1,1),(0,3)],
    "Edvaldo": [(1,0),(1,2),(1,1),(1,0),(0,3),(1,3),(1,0),(0,3),(4,0),(1,1),(1,2),(2,1),(3,1),(2,0),(1,2),(1,1),(1,0),(2,0),(1,2),(1,0),(2,1),(2,1),(2,1),(0,2),(2,1),(2,2),(1,0),(1,1),(1,1),(1,0),(1,2),(4,0),(0,1),(2,1),(2,1),(3,1),(2,0),(2,1),(2,1),(1,1),(1,2),(1,2),(2,0),(1,1),(3,1),(2,1),(0,1),(1,0),(2,1),(2,0),(1,2),(3,0),(1,2),(1,1),(0,2),(1,2),(1,2),(1,2),(2,1),(1,0),(1,1),(2,1),(0,2),(1,1),(1,2),(1,2),(1,2),(2,1),(1,1),(0,0),(1,1),(2,3)],
    "Stella": [(2,2),(2,1),(1,1),(2,1),(0,2),(0,2),(3,1),(0,3),(4,0),(0,2),(2,3),(1,1),(2,0),(1,2),(1,1),(1,1),(0,0),(2,1),(0,3),(3,0),(2,1),(0,0),(4,2),(0,2),(1,2),(2,1),(2,0),(1,2),(2,2),(2,0),(1,2),(4,0),(0,2),(2,1),(2,0),(2,0),(2,1),(3,1),(3,1),(0,2),(2,1),(2,1),(3,1),(2,2),(2,0),(1,1),(1,1),(2,3),(0,0),(2,1),(0,3),(3,0),(1,2),(2,1),(0,3),(1,3),(2,1),(0,1),(1,1),(2,1),(0,1),(3,1),(0,2),(2,2),(3,0),(1,2),(0,2),(0,0),(2,2),(3,0),(1,0),(1,3)],
    "Caravelas": [(1,1),(1,0),(1,1),(1,2),(0,2),(1,1),(2,0),(0,2),(5,0),(0,2),(0,4),(1,0),(4,0),(1,0),(1,1),(0,0),(1,0),(2,1),(0,2),(2,0),(2,0),(1,1),(2,0),(0,3),(1,1),(2,0),(0,0),(1,2),(1,1),(1,0),(1,1),(3,0),(0,2),(2,1),(3,0),(4,0),(2,0),(2,0),(2,0),(1,1),(0,0),(2,0),(3,0),(1,1),(3,0),(3,1),(1,3),(3,0),(1,1),(1,1),(0,2),(2,1),(1,2),(1,1),(1,2),(2,1),(1,1),(0,2),(1,2),(2,1),(1,1),(2,1),(0,0),(1,1),(0,0),(0,1),(0,2),(2,2),(2,1),(1,1),(1,1),(0,2)],
    "Regis": [(3,1),(0,2),(2,1),(2,2),(0,1),(0,3),(3,1),(0,3),(5,0),(1,0),(2,2),(2,0),(4,0),(4,1),(1,1),(2,1),(3,0),(4,1),(0,2),(3,0),(3,0),(3,2),(4,1),(1,2),(1,1),(4,1),(2,1),(2,1),(2,1),(1,0),(1,2),(6,0),(1,3),(3,3),(3,1),(3,0),(2,0),(2,0),(3,1),(1,2),(1,1),(2,1),(4,0),(1,1),(5,0),(2,0),(1,3),(2,2),(2,0),(1,1),(0,3),(3,0),(1,1),(1,0),(1,2),(1,3),(2,1),(1,2),(0,0),(2,1),(1,3),(2,0),(1,3),(1,1),(0,0),(0,3),(1,3),(2,1),(1,2),(1,0),(0,0),(1,2)],
    "Kardec": [(3,1),(1,1),(2,1),(1,2),(0,1),(0,2),(2,1),(0,1),(4,0),(3,2),(0,0),(2,1),(3,0),(1,0),(1,3),(1,0),(2,1),(4,1),(0,2),(2,0),(3,0),(2,1),(1,1),(0,1),(2,0),(2,1),(3,1),(1,1),(2,2),(1,0),(0,0),(4,0),(1,2),(1,0),(2,1),(3,0),(3,0),(2,0),(2,0),(0,2),(0,2),(1,0),(5,0),(1,1),(5,0),(3,1),(0,2),(2,0),(2,1),(2,1),(0,2),(4,0),(2,2),(0,1),(0,2),(0,2),(1,2),(1,2),(1,1),(2,0),(1,2),(2,0),(0,2),(1,2),(2,0),(0,2),(0,3),(2,1),(1,2),(1,0),(0,1),(0,2)],
    "Fatima": [(1,1),(1,0),(1,1),(1,2),(0,2),(1,1),(3,0),(0,2),(5,0),(0,2),(0,4),(1,0),(4,0),(1,0),(1,1),(0,0),(1,0),(2,1),(0,2),(2,0),(2,0),(1,1),(2,0),(0,3),(1,1),(2,0),(0,0),(1,2),(1,1),(1,0),(1,1),(4,0),(0,2),(2,1),(3,0),(4,0),(2,0),(2,0),(2,0),(1,1),(0,0),(2,0),(3,0),(1,1),(3,0),(3,1),(1,3),(3,0),(1,1),(1,1),(0,3),(2,1),(1,2),(1,1),(1,2),(2,1),(1,1),(0,2),(1,2),(2,1),(1,1),(2,1),(0,0),(1,1),(0,0),(0,1),(0,2),(2,2),(2,1),(1,1),(1,1),(0,2)],
    "Laurita": [(3,1),(1,1),(2,1),(1,2),(0,1),(0,2),(2,0),(0,1),(4,0),(3,2),(0,0),(2,1),(3,0),(1,0),(1,3),(1,0),(2,1),(4,1),(0,2),(2,0),(3,0),(2,1),(1,1),(0,1),(2,0),(2,1),(3,1),(1,1),(2,2),(1,0),(0,0),(3,0),(1,2),(1,0),(2,0),(3,0),(3,0),(2,0),(2,0),(0,2),(0,2),(1,0),(5,0),(1,1),(3,0),(3,1),(0,2),(2,0),(2,1),(2,1),(0,2),(4,0),(2,1),(0,1),(0,3),(0,2),(1,2),(0,2),(1,1),(2,0),(1,2),(2,0),(0,2),(1,2),(2,1),(0,2),(0,3),(2,1),(1,2),(1,0),(0,1),(0,2)],
    "Edson": [(2,0),(1,1),(0,0),(1,1),(1,1),(0,2),(2,0),(0,2),(5,0),(1,1),(2,2),(3,1),(4,0),(2,1),(1,0),(2,1),(2,0),(3,1),(0,3),(2,0),(3,0),(1,1),(3,0),(1,2),(1,1),(0,0),(1,0),(1,1),(1,1),(1,0),(1,2),(4,0),(0,2),(1,1),(2,1),(2,0),(3,0),(3,0),(1,0),(0,2),(1,2),(1,0),(3,0),(2,1),(3,1),(1,1),(0,2),(2,0),(1,1),(2,0),(1,2),(3,0),(1,1),(1,2),(0,3),(1,2),(1,1),(0,3),(1,0),(1,1),(1,1),(2,1),(0,0),(0,2),(1,0),(0,2),(1,3),(1,1),(1,1),(0,0),(1,1),(0,2)],
    "Alessandra": [(3,1),(2,1),(2,1),(2,1),(2,1),(0,2),(2,1),(1,2),(4,0),(2,1),(1,1),(1,0),(3,0),(2,0),(0,2),(2,0),(2,0),(2,1),(1,2),(3,1),(3,0),(2,1),(2,1),(0,2),(2,0),(2,1),(2,0),(1,1),(2,1),(2,1),(1,1),(4,1),(1,3),(2,2),(2,0),(2,0),(3,0),(2,1),(2,0),(0,1),(1,1),(3,1),(3,0),(1,2),(3,0),(2,1),(0,2),(3,0),(1,1),(2,1),(0,3),(2,0),(1,1),(1,1),(0,2),(1,2),(1,1),(0,2),(1,1),(2,1),(1,3),(2,0),(0,2),(1,2),(1,1),(0,3),(0,3),(1,1),(1,1),(1,1),(1,2),(0,3)],
    "Marcelo": [(1,1),(1,2),(1,1),(1,3),(1,3),(0,2),(2,1),(1,3),(4,0),(2,1),(2,2),(2,0),(2,0),(4,1),(0,1),(1,0),(2,1),(2,1),(0,3),(1,1),(2,1),(1,1),(3,1),(0,3),(1,0),(1,1),(2,1),(3,1),(1,1),(1,0),(1,1),(4,0),(1,2),(3,1),(1,2),(2,0),(3,0),(4,0),(2,1),(0,1),(1,1),(2,0),(3,0),(2,1),(4,1),(2,1),(0,4),(1,1),(2,2),(2,1),(1,3),(4,1),(1,1),(1,1),(0,2),(1,2),(1,1),(1,3),(1,1),(2,0),(1,2),(1,0),(3,1),(1,2),(0,0),(0,4),(0,3),(2,1),(1,2),(2,1),(2,1),(0,2)],
}


def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    # Initialize from spreadsheet bets, no results yet
    games = []
    for i, (dia, p1, p2) in enumerate(GAMES_RAW):
        is_brasil = "Brasil" in (p1, p2)
        bets = {}
        for participant in PARTICIPANTS:
            b = BETS_RAW[participant][i]
            bets[participant] = {"g1": b[0], "g2": b[1]}
        games.append({
            "id": i,
            "dia": dia,
            "pais1": p1,
            "pais2": p2,
            "is_brasil": is_brasil,
            "result_g1": None,
            "result_g2": None,
            "bets": bets,
        })
    data = {"games": games}
    save_data(data)
    return data


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def calc_points(r1, r2, b1, b2, scoring=None):
    """
    Calcula os pontos de uma aposta baseado no resultado real.
    
    Regras:
    - 6 pontos: Acertou o vencedor E o placar de ambas as equipes (exato)
    - 4 pontos: Acertou o vencedor E o placar de apenas uma das equipes
    - 3 pontos: Acertou o vencedor, mas não acertou o placar de nenhuma das equipes
    - 1 ponto: Não acertou o vencedor, mas acertou o placar de uma das equipes
    - 0 pontos: Não acertou nada
    """
    if r1 is None or r2 is None:
        return 0

    scoring = scoring or {
        "exact_score": 6,
        "one_goal_and_winner": 4,
        "winner_and_one_goal": 3,
        "winner_only": 1,
    }

    def winner(g1, g2):
        if g1 > g2:
            return "M"  # Mandante venceu
        if g1 < g2:
            return "V"  # Visitante venceu
        return "E"      # Empate

    rw = winner(r1, r2)
    bw = winner(b1, b2)
    
    # Verifica se acertou o placar de cada equipe
    acertou_g1 = (r1 == b1)
    acertou_g2 = (r2 == b2)

    # Caso 1: Acertou o placar exato (ambos os times)
    if acertou_g1 and acertou_g2:
        return scoring["exact_score"]  # 6 pontos

    # Caso 2: Acertou o vencedor E acertou o placar de uma das equipes
    if bw == rw and (acertou_g1 or acertou_g2):
        return scoring["one_goal_and_winner"]  # 4 pontos

    # Caso 3: Acertou o vencedor, mas não acertou nenhum placar
    if bw == rw:
        return scoring["winner_and_one_goal"]  # 3 pontos

    # Caso 4: Não acertou o vencedor, mas acertou o placar de uma das equipes
    if acertou_g1 or acertou_g2:
        return scoring["winner_only"]  # 1 ponto

    # Caso 5: Não acertou nada
    return 0


def atualizar_pontos_jogo(game, scoring=None):
    """
    Recalcula e grava a pontuação de todos os participantes
    dentro do próprio JSON do jogo.
    """

    r1 = game["result_g1"]
    r2 = game["result_g2"]

    if r1 is None or r2 is None:
        return

    for participante, aposta in game["bets"].items():

        b1 = aposta.get("g1")
        b2 = aposta.get("g2")

        if b1 is None or b2 is None:
            aposta["pontos"] = 0
            continue

        aposta["pontos"] = calc_points(
            r1,
            r2,
            b1,
            b2,
            scoring
        )


def atualizar_todos_os_pontos(data):
    scoring = data.get("scoring")

    for game in data["games"]:
        atualizar_pontos_jogo(game, scoring)

    save_data(data)


def compute_standings(data):
    """
    Calcula a classificação calculando os pontos em tempo real.
    
    Critérios de desempate (em ordem):
    1. Maior quantidade de jogos com 6 pontos
    2. Maior quantidade de jogos com 4 pontos
    3. Maior quantidade de jogos com 3 pontos
    4. Maior pontuação nos jogos do Brasil
    5. Ordem alfabética (não influencia na classificação, apenas para consistência)
    
    A posição é atribuída com base no ranking, e quando há empate em todos os critérios,
    os participantes compartilham a mesma posição.
    """

    results = {}

    for p in PARTICIPANTS:
        results[p] = {
            "total": 0,
            "pts6": 0,
            "pts4": 0,
            "pts3": 0,
            "pts1": 0,
            "brasil": 0,
            "name": p
        }

    scoring = data.get("scoring", {
        "exact_score": 6,
        "one_goal_and_winner": 4,
        "winner_and_one_goal": 3,
        "winner_only": 1,
    })

    for game in data["games"]:
        r1 = game["result_g1"]
        r2 = game["result_g2"]

        # Se não tem resultado, pula (não ganha pontos)
        if r1 is None or r2 is None:
            continue

        for p in PARTICIPANTS:
            aposta = game["bets"].get(p, {})
            b1 = aposta.get("g1")
            b2 = aposta.get("g2")

            if b1 is None or b2 is None:
                continue

            # Calcula os pontos em tempo real
            pts = calc_points(r1, r2, b1, b2, scoring)

            results[p]["total"] += pts

            if pts == scoring.get("exact_score", 6):
                results[p]["pts6"] += 1
            elif pts == scoring.get("one_goal_and_winner", 4):
                results[p]["pts4"] += 1
            elif pts == scoring.get("winner_and_one_goal", 3):
                results[p]["pts3"] += 1
            elif pts == scoring.get("winner_only", 1):
                results[p]["pts1"] += 1

            if game["is_brasil"]:
                results[p]["brasil"] += pts

    standings = []

    for p, r in results.items():
        standings.append({
            "name": p,
            "total": r["total"],
            "pts6": r["pts6"],
            "pts4": r["pts4"],
            "pts3": r["pts3"],
            "pts1": r["pts1"],
            "brasil": r["brasil"]
        })

    # Ordenação com os critérios de desempate
    standings.sort(
        key=lambda x: (
            -x["total"],      # 1. Maior pontuação total
            -x["pts6"],       # 2. Mais jogos com 6 pontos
            -x["pts4"],       # 3. Mais jogos com 4 pontos
            -x["pts3"],       # 4. Mais jogos com 3 pontos
            -x["brasil"],     # 5. Mais pontos nos jogos do Brasil
            x["name"]         # 6. Ordem alfabética (desempate final)
        )
    )

    # Atribui as posições com empatados compartilhando a mesma posição
    i = 0
    while i < len(standings):
        # Define a posição atual (baseada em 1)
        posicao = i + 1
        
        # Encontra o grupo de participantes com os mesmos critérios
        j = i
        while j < len(standings) - 1:
            # Verifica se o próximo participante tem os mesmos critérios
            atual = standings[j]
            proximo = standings[j + 1]
            
            # Compara todos os critérios de desempate
            if (atual["total"] == proximo["total"] and
                atual["pts6"] == proximo["pts6"] and
                atual["pts4"] == proximo["pts4"] and
                atual["pts3"] == proximo["pts3"] and
                atual["brasil"] == proximo["brasil"]):
                j += 1
            else:
                break
        
        # Atribui a mesma posição para todo o grupo
        for k in range(i, j + 1):
            standings[k]["rank"] = posicao
        
        # Move para o próximo grupo
        i = j + 1

    return standings