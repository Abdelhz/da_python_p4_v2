# Model

class Player:
    def __init__(self, name, ranking, gender,
                 date_of_birth, id_player, score=0):
        self.name = name
        self.ranking = ranking
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.id_player = id_player
        self.score = score

    def __str__(self):
        return self.name

    def update_score(self, point):
        self.score += point

    def update_rank(self, new_rank):
        self.ranking = new_rank

    def obj_to_dict(self):
        dic = self.__dict__
        return dic


class IdPlayers:
    def __init__(self, id_player, score, ranking):
        self.id_player = id_player
        self.score = score
        self.ranking = ranking

    def update_score(self, point):
        self.score += point


class Match:
    def __init__(self, score_1, score_2, player_1_id, player_2_id,
                 player_1_ranking, player_2_ranking, match_number):
        self.score_1 = score_1
        self.score_2 = score_2
        self.player_1_id = player_1_id
        self.player_2_id = player_2_id
        self.match_number = match_number
        self.player_1_ranking = player_1_ranking
        self.player_2_ranking = player_2_ranking


class Round:
    def __init__(self, round_number, list_matchs, start_date_time,
                 end_date_time, name_round):
        self.round_number = round_number
        self.list_matchs = list_matchs
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.name_round = name_round


class Tournament:
    def __init__(self, tournament_name, location, tournament_date_start,
                 tournament_date_end, num_of_days,
                 num_of_rounds, num_of_players, new_list_of_players,
                 list_of_rounds, tournament_state):
        self.tournament_name = tournament_name
        self.location = location
        self.tournament_date_start = tournament_date_start
        self.tournament_date_end = tournament_date_end
        self.num_of_days = num_of_days
        self.num_of_rounds = num_of_rounds
        self.num_of_players = num_of_players
        self.new_list_of_players = new_list_of_players
        self.list_of_rounds = list_of_rounds
        self.tournament_state = tournament_state

    def object_to_dic(self):
        list_of_players = self.new_list_of_players
        list_rounds = self.list_of_rounds
        new_list_of_players = []
        for player in list_of_players:
            dic_player = player.__dict__
            new_list_of_players.append(dic_player)

        new_list_rounds = []
        for round_ in list_rounds:
            new_list_matchs = []
            for match in round_.match:
                dict_match = match.__dict__
                new_list_matchs.append(dict_match)
            round_.match = new_list_matchs
            new_round = round_.__dict__
            new_list_rounds.append(new_round)

        self.list_of_rounds = new_list_rounds
        self.new_list_of_players = new_list_of_players
        dic_tournoi = self.__dict__
        return dic_tournoi
