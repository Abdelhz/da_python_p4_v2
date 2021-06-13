# Controller
import sys
import view_chess
import model_chess
import services_chess
import os
from tinydb import TinyDB, Query


class Controller:
    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(CUR_DIR, "data")
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    file = os.path.join(DATA_DIR, "db.json")
    db = TinyDB(file)
    tournois = db.table('Tournois')

    list_all_players = db.table('liste_joueurs')

    def __init__(self):
        self.view = view_chess.View()

    def create_tournament(self):
        tournament_name = self.view.get_tournament_name()
        tournament_location = self.view.get_tournament_location()
        tournament_date_start = self.view.get_tournament_date_start()
        number_rounds = self.view.get_number_rounds()
        number_players = self.view.get_number_players()

        list_of_players = self.process_players(number_players)
        list_of_players_ids = self.create_player_id(list_of_players)

        list_of_rounds, list_of_players_ids, last_round = \
            self.process_rounds(number_rounds, list_of_players_ids)

        new_list_of_players = \
            self.update_players_scores(list_of_players, list_of_players_ids)

        prompt_get_answer = \
            "Voulez-vous mettre à jour les rang des joueurs de ce tournoi ?"
        reponse = self.view.get_answer(prompt_get_answer)
        if reponse:
            new_list_of_players = \
                self.update_players_ranks(new_list_of_players)
        else:
            pass
        tournament_date_end, tournament_state, number_days = \
            self.finish_tournament(last_round, number_rounds)
        tournament = \
            model_chess.Tournament(tournament_name, tournament_location,
                                   tournament_date_start,
                                   tournament_date_end, number_days,
                                   number_rounds, number_players,
                                   new_list_of_players, list_of_rounds,
                                   tournament_state)
        return tournament, new_list_of_players

    def process_players(self, number_players):
        list_of_players = []
        for i in range(number_players):
            self.view.prompt_player_number(i + 1)
            player = self.create_player()
            list_of_players.append(player)
        return list_of_players

    def create_player(self):
        name = self.view.get_name()
        ranking = self.view.get_ranking()
        gender = self.view.get_gender()
        date_of_birth = self.view.get_date_of_birth()
        id_player = self.view.get_id_player()
        player = model_chess.Player(name, ranking, gender,
                                    date_of_birth, id_player, score=0)
        return player

    @staticmethod
    def create_player_id(list_of_players):
        list_of_players_ids = []
        for player in list_of_players:
            player_id = \
                model_chess.IdPlayers(player.id_player,
                                      player.score, player.ranking)
            list_of_players_ids.append(player_id)
        return list_of_players_ids

    def process_rounds(self, number_rounds, list_of_players_ids):
        list_of_rounds = []
        list_done_pairs = []
        last_round = -1
        for number in range(number_rounds):
            tournament_round, list_of_players_ids, list_done_pairs = \
                self.create_round(number,
                                  list_of_players_ids, list_done_pairs)
            list_of_rounds.append(tournament_round)
            prompt_get_answer = \
                f"Vous venez de terminer un round numéro" \
                f" {number + 1}, voulez-vous continuez " \
                f"le tournoi ou vous arrêtez pour l'instant" \
                f" ? oui/non ou o/n \n"
            reponse = self.view.get_answer(prompt_get_answer)
            last_round = number + 1
            if reponse:
                continue
            else:
                break
        return list_of_rounds, list_of_players_ids, last_round

    def process_last_rounds(self, number_rounds, list_of_players_ids,
                            list_of_rounds, list_done_pairs):
        last_round = list_of_rounds[-1]
        round_num = last_round.round_number
        for number in range(round_num, number_rounds):
            tournament_round, list_of_players_ids, list_done_pairs = \
                self.create_round(number, list_of_players_ids,
                                  list_done_pairs)
            list_of_rounds.append(tournament_round)
            prompt_get_answer = \
                f"Vous venez de terminer un round numéro " \
                f"{number + 1}, voulez-vous continuez " \
                f"le tournoi ou vous arrêtez pour l'instant " \
                f"? oui/non ou o/n \n"
            reponse = self.view.get_answer(prompt_get_answer)
            last_round = number + 1
            if reponse:
                continue
            else:
                break
        return list_of_rounds, list_of_players_ids, last_round

    def create_round(self, number, list_of_players_ids, list_done_pairs):
        round_number = number + 1
        start_date_time = self.view.get_round_start_time()
        end_date_time = self.view.get_round_end_time()
        name_round = self.view.get_round_name()
        list_of_matches, list_of_players_ids, list_done_pairs = \
            self.create_matchs(list_of_players_ids, round_number,
                               list_done_pairs)
        tournament_round = \
            model_chess.Round(round_number,
                              list_of_matches, start_date_time, end_date_time,
                              name_round)
        return tournament_round, list_of_players_ids, list_done_pairs

    def create_matchs(self, list_of_players_ids, round_number,
                      list_done_pairs):
        list_players_sorted = \
            services_chess.sorting_list_score(list_of_players_ids)
        if round_number < 2:
            list_of_pairs, list_done_pairs = \
                self.create_pairs(list_players_sorted, list_done_pairs)
        else:
            list_of_pairs, list_done_pairs = \
                self.create_new_pairs(list_players_sorted, list_done_pairs)
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
            match = \
                model_chess.Match(score_1, score_2, pairs[0].id_player,
                                  pairs[1].id_player, pairs[0].ranking,
                                  pairs[1].ranking, str(match_number))
            list_of_matches.append(match)

        return list_of_matches, list_of_players_ids, list_done_pairs

    @staticmethod
    def create_pairs(list_of_players_sorted, list_done_pairs):
        list_of_pairs, list_done_pairs = \
            services_chess.create_pairs(list_of_players_sorted,
                                        list_done_pairs)
        return list_of_pairs, list_done_pairs

    @staticmethod
    def create_new_pairs(list_players_sorted, list_done_pairs):
        list_of_pairs, list_done_pairs = \
            services_chess.create_new_pairs(list_players_sorted,
                                            list_done_pairs)
        return list_of_pairs, list_done_pairs

    @staticmethod
    def update_players_scores(list_of_players, list_of_players_ids):
        for player in list_of_players:
            for p_id in list_of_players_ids:
                if player.id_player == p_id.id_player:
                    player.update_score(p_id.score)
                    break
                pass
        return list_of_players

    def update_players_ranks(self, list_of_players):
        for player in list_of_players:
            self.view.prompt_player_details(player)
            new_rank = self.view.get_ranking()
            player.update_rank(new_rank)
        return list_of_players

    def finish_tournament(self, last_round, number_rounds):
        if last_round < number_rounds:
            tournament_date_end = ""
            tournament_state = "non fini"
            number_days = ""
        else:
            tournament_date_end = self.view.get_tournament_date_end()
            number_days = self.view.get_number_days()
            tournament_state = "fini"
        return tournament_date_end, tournament_state, number_days

    @staticmethod
    def obj_to_dic_players(list_of_players):
        list_dic_players = []
        for player in list_of_players:
            dic_player = player.__dict__
            list_dic_players.append(dic_player)
        return list_dic_players

    @staticmethod
    def obj_to_dic_rounds(list_rounds):
        dic_list_rounds = []
        for a_round in list_rounds:
            new_list_matchs = []
            for match in a_round.list_matchs:
                dict_match = match.__dict__
                new_list_matchs.append(dict_match)
            a_round.list_matchs = new_list_matchs
            new_round = a_round.__dict__
            dic_list_rounds.append(new_round)
        return dic_list_rounds

    def obj_to_dic_tournament(self, tournament):
        list_of_players = tournament.new_list_of_players
        new_list_of_players = self.obj_to_dic_players(list_of_players)

        list_rounds = tournament.list_of_rounds
        new_list_rounds = self.obj_to_dic_rounds(list_rounds)

        tournament.list_of_rounds = new_list_rounds
        tournament.new_list_of_players = new_list_of_players
        dic_tournoi = tournament.__dict__
        return dic_tournoi

    def insert_players(self, new_list_of_players):
        list_dic_players = self.obj_to_dic_players(new_list_of_players)
        for dic_player in list_dic_players:
            player = self.list_all_players.search(Query().id_player ==
                                                  dic_player['id_player'])
            if not player:
                self.list_all_players.insert(dic_player)
            else:
                self.list_all_players.update({"ranking": dic_player['ranking'],
                                              "score": dic_player['score']},
                                             Query().id_player ==
                                             dic_player['id_player'])
        # inserer nouveau joueurs sinon mettre à jour

    def insert_tournament(self, tournament):
        dic_tournoi = self.obj_to_dic_tournament(tournament)
        tournoi = self.tournois.search(Query().tournament_name ==
                                       dic_tournoi['tournament_name'])
        if not tournoi:
            self.tournois.insert(dic_tournoi)
        else:
            self.tournois.update(
                {"tournament_date_end": dic_tournoi['tournament_date_end'],
                 "num_of_days": dic_tournoi['num_of_days']},
                Query().tournament_name == dic_tournoi['tournament_name'])
            self.tournois.update(
                {"new_list_of_players": dic_tournoi['new_list_of_players'],
                 "list_of_rounds": dic_tournoi['list_of_rounds']},
                Query().tournament_name == dic_tournoi['tournament_name'])
            self.tournois.update(
                {"tournament_state": dic_tournoi['tournament_state']},
                Query().tournament_name == dic_tournoi['tournament_name'])

    def continue_tournament(self, last_tournament):
        tournament, list_of_players, number_rounds, list_done_pairs = \
            self.dic_tournament_to_obj(last_tournament)
        list_of_rounds = tournament.list_of_rounds
        list_of_players_ids = self.create_player_id(list_of_players)
        list_of_rounds, list_of_players_ids, last_round = \
            self.process_last_rounds(tournament.num_of_rounds,
                                     list_of_players_ids,
                                     list_of_rounds, list_done_pairs)
        new_list_of_players = \
            self.update_players_scores(list_of_players, list_of_players_ids)

        prompt_get_answer = \
            "Voulez-vous mettre à jour les rang des joueurs de ce tournoi ?"
        reponse = self.view.get_answer(prompt_get_answer)
        if reponse:
            new_list_of_players = \
                self.update_players_ranks(new_list_of_players)
        else:
            pass
        tournament_date_end, tournament_state, number_days = \
            self.finish_tournament(last_round, number_rounds)
        tournament.list_of_rounds = list_of_rounds
        tournament.new_list_of_players = new_list_of_players
        tournament.tournament_date_end = tournament_date_end
        tournament.tournament_state = tournament_state
        tournament.num_of_days = number_days
        return tournament, new_list_of_players

    @staticmethod
    def update_list_players(list_of_players):
        return list_of_players

    def menu(self):
        answer = self.view.get_menu_option()
        if answer == "1":
            tournament, new_list_of_players = self.create_tournament()
            self.insert_players(new_list_of_players)
            self.insert_tournament(tournament)

        elif answer == "2":
            self.search_unfinished_tournaments()

        elif answer == "3":
            self.search_player()

        elif answer == "4":
            sys.exit("Fermeture du programme !")

        return self.menu()

    def search_unfinished_tournaments(self):
        try:
            unfinished_tournaments = \
                self.tournois.search(Query().tournament_state == 'non fini')
            if not unfinished_tournaments:
                prompt = "Il n'y a aucun tournoi non fini !\n"
                self.view.prompt_prompt(prompt)
                return self.menu()
            else:
                last_tournament = \
                    self.choose_tournament(unfinished_tournaments)
                tournament, new_list_of_players = \
                    self.continue_tournament(last_tournament)
                self.insert_tournament(tournament)
                self.insert_players(new_list_of_players)
                return self.menu()
        except ValueError:
            prompt = "Il y eu une erreur, Veuillez recommencer !"
            self.view.prompt_prompt(prompt)
            return self.menu()

    def search_player(self):
        joueurs = self.list_all_players.all()
        for joueur in joueurs:
            prompt_0 = \
                f"{joueur['name']} avec l'ID {joueur['id_player']} " \
                f"et un rang de {joueur['ranking']}\n"
            self.view.prompt_prompt(prompt_0)
        prompt_1 = "Voulez-vous modifier les joueurs ?\n"
        prompt = "Donnez le nom du joueur à modifier :"
        answer = self.view.get_answer(prompt_1)
        if answer:
            try:
                nom_joueur = self.view.get_answer_2(prompt)
                joueur = \
                    self.list_all_players.search(Query().name == nom_joueur)
                if not joueur:
                    prompt_1 = "ce nom n'existe pas dans la liste," \
                               " veuillez recommencer !\n"
                    self.view.prompt_prompt(prompt_1)
                    return self.search_player()
                else:
                    prompt_1 = "Donnez le nouveau rang du joueur :\n"
                    ranking = int(self.view.get_answer_2(prompt_1))
                    self.list_all_players.update({"ranking": ranking},
                                                 Query().name == nom_joueur)
                    prompt_2 = \
                        "Voulez-vous continuer à modifier des joueurs ?\n"
                    answer = self.view.get_answer(prompt_2)
                    if answer:
                        return self.search_player()
                    else:
                        pass
            except SyntaxError:
                prompt_3 = \
                    "Le nom du joueur saisie est incorrecte, " \
                    "veuillez recommencer"
                self.view.prompt_prompt(prompt_3)
                return self.search_player()
        else:
            self.menu()

    def choose_tournament(self, unfinished_tournaments):
        prompt = "Voici les noms des tournois non fini :\n"
        self.view.prompt_prompt(prompt)
        for unfinished_tournament in unfinished_tournaments:
            self.view.prompt_prompt(unfinished_tournament['tournament_name'])
        try:
            prompt_1 = "Saisissez le nom du tournoi à finir :\n"
            answer = self.view.get_answer_2(prompt_1)
            tournament = \
                self.tournois.search(Query().tournament_name == answer)
            if not tournament:
                prompt_2 = \
                    "Vous vous êtes trompé de saisie ! Veuillez recommencer !"
                self.view.prompt_prompt(prompt_2)
                return self.choose_tournament(unfinished_tournaments)
            else:
                last_tournament = tournament[0]
                return last_tournament
        except SyntaxError:
            prompt_3 = \
                "Vous vous êtes trompé de saisie ! Veuillez recommencer !"
            self.view.prompt_prompt(prompt_3)
            return self.choose_tournament(unfinished_tournaments)

    @staticmethod
    def dic_players_to_obj(dic_list_of_players):
        new_list_of_players = []
        for player_dic in dic_list_of_players:
            name = player_dic['name']
            ranking = player_dic['ranking']
            gender = player_dic['gender']
            date_of_birth = player_dic['date_of_birth']
            id_player = player_dic['id_player']
            score = player_dic['score']
            player = \
                model_chess.Player(name, ranking,
                                   gender, date_of_birth, id_player, score)
            new_list_of_players.append(player)
        return new_list_of_players

    @staticmethod
    def dic_rounds_to_obj(dic_list_of_rounds):
        list_of_rounds = []
        list_done_pairs = []
        for dic_round in dic_list_of_rounds:
            round_number = dic_round['round_number']
            start_date_time = dic_round['start_date_time']
            end_date_time = dic_round['end_date_time']
            name_round = dic_round['name_round']
            dic_matchs = dic_round['list_matchs']
            new_match = []
            for match in dic_matchs:
                score_1 = match['score_1']
                score_2 = match['score_2']
                player_1_id = match['player_1_id']
                player_2_id = match['player_2_id']
                player_1_ranking = match['player_1_ranking']
                player_2_ranking = match['player_2_ranking']
                match_number = match['match_number']
                match = \
                    model_chess.Match(score_1,
                                      score_2, player_1_id, player_2_id,
                                      player_1_ranking,
                                      player_1_ranking, str(match_number))
                player_1 = \
                    model_chess.IdPlayers(player_1_id,
                                          score_1, player_1_ranking)
                player_2 = \
                    model_chess.IdPlayers(player_2_id,
                                          score_2, player_2_ranking)
                pair = [player_1, player_2]
                list_done_pairs.append(pair)
                new_match.append(match)
            tournament_round = \
                model_chess.Round(round_number, new_match,
                                  start_date_time,
                                  end_date_time, name_round)
            list_of_rounds.append(tournament_round)
        return list_of_rounds, list_done_pairs

    def dic_tournament_to_obj(self, dic_tournament):
        tournament_name = dic_tournament["tournament_name"]
        location = dic_tournament["location"]
        tournament_date_start = dic_tournament["tournament_date_start"]
        tournament_date_end = dic_tournament["tournament_date_end"]
        num_of_days = dic_tournament["num_of_days"]
        num_of_rounds = dic_tournament["num_of_rounds"]
        num_of_players = dic_tournament["num_of_players"]
        dic_list_of_players = dic_tournament["new_list_of_players"]
        dic_list_of_rounds = dic_tournament["list_of_rounds"]
        tournament_state = dic_tournament["tournament_state"]
        new_list_of_players = self.dic_players_to_obj(dic_list_of_players)
        list_of_rounds, list_done_pairs = \
            self.dic_rounds_to_obj(dic_list_of_rounds)

        tournament = \
            model_chess.Tournament(tournament_name,
                                   location, tournament_date_start,
                                   tournament_date_end,
                                   num_of_days, num_of_rounds, num_of_players,
                                   new_list_of_players,
                                   list_of_rounds, tournament_state)
        return tournament, new_list_of_players, num_of_rounds, list_done_pairs
