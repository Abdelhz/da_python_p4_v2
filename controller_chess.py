# Controller
import view_chess
import model_chess
import services_chess


class Controller:
    def __init__(self):
        self.view = view_chess.View()

    def create_tournament(self):
        tournament_name = self.view.get_tournament_name()
        tournament_location = self.view.get_tournament_location()
        tournament_date_start = self.view.get_tournament_date_start()
        tournament_date_end = self.view.get_tournament_date_end()
        number_days = self.view.get_number_days()
        number_rounds = self.view.get_number_rounds()
        number_players = self.view.get_number_players()
        list_of_players = []
        for i in range(number_players):
            player = self.create_player()
            list_of_players.append(player)

        list_of_players_ids = self.create_player_id(list_of_players)

        list_of_rounds = []
        list_done_pairs = []
        for number in range(number_rounds):
            tournament_round, list_of_players_ids, list_done_pairs = self.create_round(number, list_of_players_ids,
                                                                                       list_done_pairs)
            list_of_rounds.append(tournament_round)

        tournament = model_chess.Tournament(tournament_name, tournament_location, tournament_date_start,
                                            tournament_date_end, number_days, number_rounds, number_players,
                                            list_of_players, list_of_rounds)
        return tournament

    def create_player(self):
        name = self.view.get_name()
        ranking = self.view.get_ranking()
        gender = self.view.get_gender()
        date_of_birth = self.view.get_date_of_birth()
        id_player = self.view.get_id_player()

        player = model_chess.Player(name, ranking, gender, date_of_birth, id_player, score=0)
        return player

    @staticmethod
    def create_player_id(list_of_players):
        list_of_players_ids = []
        for player in list_of_players:
            player_id = model_chess.IdPlayers(player.ranking, player.id_player, player.score)
            list_of_players_ids.append(player_id)

        return list_of_players_ids

    def create_round(self, number, list_of_players_ids, list_done_pairs):
        round_number = number
        start_date_time = self.view.get_round_start_time()
        end_date_time = self.view.get_round_end_time()
        name_round = self.view.get_round_name()
        list_of_matches, list_of_players_ids, list_done_pairs = self.create_matchs(list_of_players_ids, round_number,
                                                                                   list_done_pairs)
        tournament_round = model_chess.Round(round_number, list_of_matches, start_date_time, end_date_time,
                                             name_round)
        return tournament_round, list_of_players_ids, list_done_pairs

    def create_matchs(self, list_of_players_ids, round_number, list_done_pairs):
        list_players_sorted = services_chess.sorting_list_score(list_of_players_ids)
        if round_number < 2:
            list_of_pairs, list_done_pairs = self.create_pairs(list_players_sorted, list_done_pairs)
        else:
            list_of_pairs, list_done_pairs = self.create_new_pairs(list_players_sorted, list_done_pairs)
        list_of_matches = []
        match_number = 0
        for pairs in list_of_pairs:
            match_number += 1
            score_1 = self.view.get_score_player(pairs[0].id_player)
            score_2 = self.view.get_score_player(pairs[1].id_player)
            pairs[0].update_score(score_1)
            pairs[1].update_score(score_2)
            for player_id in list_of_players_ids:
                if player_id.id_player == pairs[0].id_player:
                    player_id.score = pairs[0].score
                elif player_id.id_player == pairs[1].id_player:
                    player_id.score = pairs[1].score
                pass
            match = model_chess.Match(score_1, score_2, pairs[0], pairs[1], str(match_number))
            list_of_matches.append(match)

        return list_of_matches, list_of_players_ids, list_done_pairs

    @staticmethod
    def create_pairs(list_of_players_sorted, list_done_pairs):
        list_of_pairs = services_chess.create_pairs(list_of_players_sorted, list_done_pairs)
        return list_of_pairs, list_done_pairs

    @staticmethod
    def create_new_pairs(list_of_players_sorted, list_done_pairs):
        list_of_pairs, list_done_pairs = services_chess.create_new_pairs(list_of_players_sorted, list_done_pairs)
        return list_of_pairs, list_done_pairs

    """
        number_of_players = int(input("Give the number of players participating : "))
        print(number_of_players)
        if (number_of_players % 2) == 0:
            n_o_p = number_of_players
        else:
            n_o_p = number_of_players - 1
        print(n_o_p)
    
    
        for i in range(n_o_p):
            player = controller_ch.create_player()
            list_of_players.append(player)
            print(i)
    """
