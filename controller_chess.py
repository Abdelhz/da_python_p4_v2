# Controller
import view_chess
import model_chess
import services_chess


class Controller:
    def __init__(self):
        self.view = view_chess.View()

    def create_player(self):
        name = self.view.get_name()
        ranking = self.view.get_ranking()
        elo = self.view.get_elo()
        gender = self.view.get_gender()
        date_of_birth = self.view.get_date_of_birth()
        id_player = self.view.get_id_player()

        player = model_chess.Player(name, ranking, elo, gender, date_of_birth, id_player)
        return player

    def create_matchs(self, list_of_players):
        list_players_sorted = services_chess.sorting_list(list_of_players)
        list_of_pairs = services_chess.create_pairs(list_players_sorted)
        list_of_matches = []
        for pairs in list_of_pairs:
            score = int(input("Donner un score au matche"))
            match = [pairs[0], pairs[1], score]
            list_of_matches.append(match)
        return list_of_matches
