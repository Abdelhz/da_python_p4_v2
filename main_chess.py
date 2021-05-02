import os
from controller_chess import Controller
from tinydb import TinyDB, Query

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CUR_DIR, "data")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
file = os.path.join(DATA_DIR, "db.json")

db = TinyDB(file)


controller_ch = Controller()
if __name__ == "__main__":
    tournament = controller_ch.create_tournament()
    list_of_players = tournament.new_list_of_players
    for player in list_of_players:
        print(f"Le joueur {player.name} a un score de {player.score} et un tank de {player.ranking}\n\n")

    list_rounds = tournament.list_of_rounds
    new_list_of_players = []
    for player in list_of_players:
        dic_player = player.__dict__
        new_list_of_players.append(dic_player)

    new_list_rounds = []
    for round in list_rounds:
        new_list_matchs = []
        for match in round.match:
            dict_match = match.__dict__
            new_list_matchs.append(dict_match)
        round.match = new_list_matchs
        new_round = round.__dict__
        new_list_rounds.append(new_round)

    tournament.list_of_rounds = new_list_rounds
    tournament.new_list_of_players = new_list_of_players
    dic_tournoi = tournament.__dict__

    print(dic_tournoi)
    print("\n\n\n")
    print(dic_tournoi.get('new_list_of_players'))
    db.insert(dic_tournoi)