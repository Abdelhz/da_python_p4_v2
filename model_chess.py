# Model

class Player:
    def __init__(self, name, ranking, elo, gender, date_of_birth, id_player):
        self.name = name
        self.ranking = ranking
        self.elo = elo
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.id_player = id_player

    def __str__(self):
        return self.name


class Match:
    def __init__(self, score, id_p1, id_p2):
        self.score = score
        self.id_p1 = id_p1
        self.id_p2 = id_p2


class Round:
    def __init__(self, match, start_date_time, end_date_time, name_round):
        self.match = match
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.name_round = name_round


class Tournament:
    def __init__(self, name_tournament, location, date, num_of_days, num_of_rounds, num_of_players):
        self.name_tournament = name_tournament
        self.location = location
        self.date = date
        self.num_of_days = num_of_days
        self.num_of_rounds = num_of_rounds
        self.num_of_players = num_of_players


class Pairs:
    def __init__(self, player_1_id, player_2_id):
        self.player_1_id = player_1_id
        self.player_2_id = player_2_id
