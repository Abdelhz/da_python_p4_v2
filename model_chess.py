# Model

class Player:
    def __init__(self, name, ranking, gender, date_of_birth, id_player, score=0):
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

    def update_rank(self, points):
        self.ranking += points


class IdPlayers:
    def __init__(self, ranking, id_player, score):
        self.ranking = ranking
        self.id_player = id_player
        self.score = score

    def update_score(self, point):
        self.score += point


class Pairs:
    def __init__(self, player_1_id, player_2_id):
        self.player_1_id = player_1_id
        self.player_2_id = player_2_id


class Match:
    def __init__(self, score_1, score_2, player_1_id, player_2_id, match_number):
        self.score_1 = score_1
        self.score_2 = score_2
        self.player_1_id = player_1_id
        self.player_2_id = player_2_id
        self.match_number = match_number


class Round:
    def __init__(self, round_number, match, start_date_time, end_date_time, name_round):
        self.round_number = round_number
        self.match = match
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.name_round = name_round


class Tournament:
    def __init__(self, tournament_name, location, tournament_date_start, tournament_date_end, num_of_days,
                 num_of_rounds, num_of_players, new_list_of_players, list_of_rounds):
        self.tournament_name = tournament_name
        self.location = location
        self.tournament_date_start = tournament_date_start
        self.tournament_date_end = tournament_date_end
        self.num_of_days = num_of_days
        self.num_of_rounds = num_of_rounds
        self.num_of_players = num_of_players
        self.new_list_of_players = new_list_of_players
        self.list_of_rounds = list_of_rounds
