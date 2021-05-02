from controller_chess import Controller

controller_ch = Controller()
if __name__ == "__main__":
    tournament = controller_ch.create_tournament()
    list_of_players = tournament.new_list_of_players
    for player in list_of_players:
        print(f"Le joueur {player.name} a un score de {player.score} et un tank de {player.ranking}\n\n")