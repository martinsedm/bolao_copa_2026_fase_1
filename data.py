# data.py - versão completamente corrigida
import json
import os
from pathlib import Path

DATA_FILE = Path(__file__).parent / "bolao_data.json"
BACKUP_FILE = Path(__file__).parent / "bolao_data_backup.json"

PARTICIPANTS = [
    "Edmilson", "Cesare", "Daiane", "Julio", "Edvaldo",
    "Stella", "Caravelas", "Regis", "Kardec", "Fatima",
    "Laurita", "Edson", "Alessandra", "Marcelo"
]

BRASIL_TEAMS = {"Brasil"}

GAMES_RAW = [
    (11, "Mexico", "Africa do Sul"),
    (11, "Coreia do Sul", "Republica Tcheca"),
    (12, "Canada", "Bosnia-Herzegovina"),
    (12, "Estados Unidos", "Paraguai"),
    (14, "Australia", "Turquia"),
    (13, "Qatar", "Suica"),
    (13, "Brasil", "Marrocos"),
    (13, "Haiti", "Escocia"),
    (14, "Alemanha", "Curacao"),
    (14, "Holanda", "Japao"),
    (14, "Costa do Marfim", "Equador"),
    (14, "Suecia", "Tunisia"),
    (15, "Espanha", "Cabo Verde"),
    (15, "Belgica", "Egito"),
    (15, "Arabia Saudita", "Uruguai"),
    (15, "Iran", "Nova Zelandia"),
    (17, "Austria", "Jordania"),
    (16, "Franca", "Senegal"),
    (16, "Iraque", "Noruega"),
    (16, "Argentina", "Argelia"),
    (17, "Portugal", "Congo (RD)"),
    (17, "Inglaterra", "Croacia"),
    (17, "Gana", "Panama"),
    (17, "Uzbequistao", "Colombia"),
    (18, "Republica Tcheca", "Africa do Sul"),
    (18, "Suica", "Bosnia-Herzegovina"),
    (18, "Canada", "Qatar"),
    (18, "Mexico", "Coreia do Sul"),
    (19, "Turquia", "Paraguai"),
    (19, "Estados Unidos", "Australia"),
    (19, "Escocia", "Marrocos"),
    (19, "Brasil", "Haiti"),
    (20, "Tunisia", "Japao"),
    (20, "Holanda", "Suecia"),
    (20, "Alemanha", "Costa do Marfim"),
    (20, "Equador", "Curacao"),
    (21, "Espanha", "Arabia Saudita"),
    (21, "Belgica", "Iran"),
    (21, "Uruguai", "Cabo Verde"),
    (21, "Nova Zelandia", "Egito"),
    (23, "Jordania", "Argelia"),
    (22, "Argentina", "Austria"),
    (22, "Franca", "Iraque"),
    (22, "Noruega", "Senegal"),
    (23, "Portugal", "Uzbequistao"),
    (23, "Inglaterra", "Gana"),
    (23, "Panama", "Croacia"),
    (23, "Colombia", "Congo (RD)"),
    (24, "Suica", "Canada"),
    (24, "Bosnia-Herzegovina", "Qatar"),
    (24, "Escocia", "Brasil"),
    (24, "Marrocos", "Haiti"),
    (24, "Republica Tcheca", "Mexico"),
    (24, "Africa do Sul", "Coreia do Sul"),
    (25, "Curacao", "Costa do Marfim"),
    (25, "Equador", "Alemanha"),
    (25, "Japao", "Suecia"),
    (25, "Tunisia", "Holanda"),
    (25, "Turquia", "Estados Unidos"),
    (25, "Paraguai", "Australia"),
    (26, "Noruega", "Franca"),
    (26, "Senegal", "Iraque"),
    (26, "Cabo Verde", "Arabia Saudita"),
    (26, "Uruguai", "Espanha"),
    (27, "Egito", "Iran"),
    (27, "Nova Zelandia", "Belgica"),
    (27, "Panama", "Inglaterra"),
    (27, "Croacia", "Gana"),
    (27, "Colombia", "Portugal"),
    (27, "Congo (RD)", "Uzbequistao"),
    (27, "Argelia", "Austria"),
    (27, "Jordania", "Argentina"),
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


def criar_dados_padrao():
    """Cria a estrutura de dados padrão (sem resultados)"""
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
    return {"games": games}


def load_data():
    # Se o arquivo não existe, cria um novo
    if not DATA_FILE.exists():
        data = criar_dados_padrao()
        save_data(data)
        return data

    # Tenta ler o arquivo existente
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        print(f"Erro ao ler arquivo: {e}")
        
        # Tenta fazer backup do arquivo corrompido
        try:
            import shutil
            shutil.copy2(DATA_FILE, BACKUP_FILE)
            print(f"Backup criado em: {BACKUP_FILE}")
        except:
            pass
        
        # Tenta ler com outros encodings
        encodings = ['latin-1', 'cp1252', 'iso-8859-1']
        for encoding in encodings:
            try:
                with open(DATA_FILE, "r", encoding=encoding) as f:
                    data = json.load(f)
                    # Salva novamente em UTF-8
                    save_data(data)
                    print(f"Arquivo recuperado com encoding {encoding}")
                    return data
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue
        
        # Se ainda falhar, cria um novo arquivo
        print("Arquivo corrompido. Criando novo arquivo de dados...")
        data = criar_dados_padrao()
        save_data(data)
        return data


def save_data(data):
    """Salva os dados em formato JSON com encoding UTF-8"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def calc_points(r1, r2, b1, b2, scoring=None):
    """
    Calcula os pontos de uma aposta baseado no resultado real.
    
    Regras:
    - 6 pontos: Acertou o vencedor E o placar de ambas as equipes (exato)
    - 4 pontos: Acertou o vencedor E o placar de apenas uma das equipes
    - 3 pontos: Acertou o vencedor, mas nao acertou o placar de nenhuma das equipes
    - 1 ponto: Nao acertou o vencedor, mas acertou o placar de uma das equipes
    - 0 pontos: Nao acertou nada
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

    # Caso 3: Acertou o vencedor, mas nao acertou nenhum placar
    if bw == rw:
        return scoring["winner_and_one_goal"]  # 3 pontos

    # Caso 4: Nao acertou o vencedor, mas acertou o placar de uma das equipes
    if acertou_g1 or acertou_g2:
        return scoring["winner_only"]  # 1 ponto

    # Caso 5: Nao acertou nada
    return 0


def atualizar_pontos_jogo(game, scoring=None):
    """
    Recalcula e grava a pontuacao de todos os participantes
    dentro do proprio JSON do jogo.
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
    Calcula a classificacao calculando os pontos em tempo real.
    
    Criterios de desempate (em ordem):
    1. Maior quantidade de jogos com 6 pontos
    2. Maior quantidade de jogos com 4 pontos
    3. Maior quantidade de jogos com 3 pontos
    4. Maior pontuacao nos jogos do Brasil
    5. Ordem alfabetica (nao influencia na classificacao, apenas para consistencia)
    
    A posicao e atribuida com base no ranking, e quando ha empate em todos os criterios,
    os participantes compartilham a mesma posicao.
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

        # Se nao tem resultado, pula (nao ganha pontos)
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

    # Ordenacao com os criterios de desempate
    standings.sort(
        key=lambda x: (
            -x["total"],      # 1. Maior pontuacao total
            -x["pts6"],       # 2. Mais jogos com 6 pontos
            -x["pts4"],       # 3. Mais jogos com 4 pontos
            -x["pts3"],       # 4. Mais jogos com 3 pontos
            -x["brasil"],     # 5. Mais pontos nos jogos do Brasil
            x["name"]         # 6. Ordem alfabetica (desempate final)
        )
    )

    # Atribui as posicoes com empatados compartilhando a mesma posicao
    i = 0
    while i < len(standings):
        # Define a posicao atual (baseada em 1)
        posicao = i + 1
        
        # Encontra o grupo de participantes com os mesmos criterios
        j = i
        while j < len(standings) - 1:
            # Verifica se o proximo participante tem os mesmos criterios
            atual = standings[j]
            proximo = standings[j + 1]
            
            # Compara todos os criterios de desempate
            if (atual["total"] == proximo["total"] and
                atual["pts6"] == proximo["pts6"] and
                atual["pts4"] == proximo["pts4"] and
                atual["pts3"] == proximo["pts3"] and
                atual["brasil"] == proximo["brasil"]):
                j += 1
            else:
                break
        
        # Atribui a mesma posicao para todo o grupo
        for k in range(i, j + 1):
            standings[k]["rank"] = posicao
        
        # Move para o proximo grupo
        i = j + 1

    return standings