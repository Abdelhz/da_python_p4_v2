# View
class View:

    @staticmethod
    def prompt_player_number(player_number):
        print(f"Saisissez les information pour le joueur numéro {player_number} :")

    def get_name(self):
        try:
            name = input("Saisissez le nom du joueur :\n\n")
            if len(name) > 20:
                print("Le nom est trop long !\n")
                return self.get_name()
            return name

        except SyntaxError:
            print("Erreur de syntaxe, veuillez recommencer !\n")
            return self.get_name()

    def get_ranking(self):
        try:
            ranking = int(input("Saisissez le rang du joueur\n\n"))
            if len(str(ranking)) > 4:
                print("La valeur saisie esr trop longue !\n")
                return self.get_ranking()
            return ranking

        except ValueError:  # if string is passed as int
            print("Saisissez seulement des nombres !\n\n")
            return self.get_ranking()

    def get_gender(self):
        try:
            gender = input("Saisissez le genre du joueur homme : h ou femme : f \n\n")
            if len(gender) > 1:
                print("La valeur saisie esr trop longue !\n")
                return self.get_gender()
            return gender

        except SyntaxError:
            print("Erreur de syntaxe, veuillez recommencer !\n")
            return self.get_gender()

    def get_date_of_birth(self):
        try:
            date_of_birth = input("Saisissez la date de naissance du joueur, comme suit : jj/mm/aaaa\n\n")
            if len(date_of_birth) > 10:
                print("La valeur saisie est trop longue !\n")
                return self.get_date_of_birth()
            return date_of_birth

        except SyntaxError:  # if string is passed as int
            print("Saisissez la date de naissance comme montré\n\n")
            return self.get_date_of_birth()

    def get_id_player(self):
        try:
            id_player = int(input("Saisissez un ID à 4 chiffres\n\n"))
            if len(str(id_player)) != 4:
                print("La valeur saisie n'a pas la bonne taille !\n")
                return self.get_id_player()
            return id_player

        except ValueError:  # if int is passed as string
            print("Saisissez seulement des nombres !\n\n")
            return self.get_id_player()

    def get_tournament_name(self):
        try:
            tournament_name = input("Saisissez un nom de tournoi :\n\n")
            if len(tournament_name) > 20:
                print("La valeur saisie est trop longue !\n")
                return self.get_tournament_name()
            return tournament_name

        except SyntaxError:
            print("Erreur de syntaxe, veuillez recommencer !\n")
            return self.get_tournament_name()

    def get_number_rounds(self):
        try:
            number_of_rounds = int(input("Donnez le nombre de tours\n\n"))
            if len(str(number_of_rounds)) > 1:
                print("La valeur saisie est trop longue !\n")
                return self.get_number_rounds()
            return number_of_rounds

        except ValueError:  # if int is passed as string
            print("Saisissez seulement des nombres !\n\n")
            return self.get_number_rounds()

    def get_tournament_location(self):
        try:
            tournament_location = input("Indiquez ou se déroule le tournoi :\n\n")
            if len(tournament_location) > 20:
                print("La valeur saisie est trop longue !\n")
                return self.get_tournament_location()
            return tournament_location

        except SyntaxError:
            print("Erreur de syntaxe, veuillez recommencer !\n")
            return self.get_tournament_location()

    def get_tournament_date_start(self):
        try:
            tournament_date_start = input("Indiquez la date de debut du tournoi comme suit : jj/mm/aaaa\n\n")
            if len(tournament_date_start) > 10:
                print("La valeur saisie est trop longue !\n")
                return self.get_tournament_date_start()
            return tournament_date_start

        except SyntaxError:  # if not written correctly
            print("Saisissez la date comme montré !\n\n")
            return self.get_tournament_date_start()

    def get_tournament_date_end(self):
        try:
            tournament_date_end = input("Indiquez la date de fin du tournoi comme suit : jj/mm/aaaa\n\n")
            if len(tournament_date_end) > 10:
                print("La valeur saisie est trop longue !\n")
                return self.get_tournament_date_end()
            return tournament_date_end

        except SyntaxError:  # if not written correctly
            print("Saisissez la date comme montré !\n\n")
            return self.get_tournament_date_end()

    def get_number_days(self):
        try:
            number_days = int(input("Indiquez le nombre de jours durant lesquels se déroulera le tournoi :\n\n"))
            if len(str(number_days)) > 2:
                print("La valeur saisie est trop longue !\n")
                return self.get_number_days()
            return number_days

        except ValueError:  # if int is passed as string
            print("Saisissez seulement des nombres !\n\n")
            return self.get_number_days()

    def get_number_players(self):
        try:
            number_players = int(input("Indiquez le nombre de joueurs participant au tournoi :\n\n"))
            if len(str(number_players)) > 2:
                print("La valeur saisie est trop longue !\n")
                return self.get_number_players()
            return number_players

        except ValueError:  # if int is passed as string
            print("Saisissez seulement des nombres !\n\n")
            return self.get_number_players()

    def get_round_start_time(self):
        try:
            round_start_time = input("Indiquez la date et heure de debut du tour : jj/mm/aaaa hh:mm\n\n")
            if len(round_start_time) > 16:
                return self.get_round_start_time()
            return round_start_time

        except SyntaxError:  # if not written correctly
            print("Saisissez la date et heure comme montré !\n\n")
            return self.get_round_start_time()

    def get_round_end_time(self):
        try:
            round_end_time = input("Indiquez la date et heure de fin du tour : jj/mm/aaaa hh:mm\n\n")
            if len(round_end_time) > 16:
                return self.get_round_end_time()
            return round_end_time

        except SyntaxError:  # if not written correctly
            print("Saisissez la date et heure comme montré !\n\n")
            return self.get_round_end_time()

    def get_round_name(self):
        try:
            round_name = input("Saisissez le nom du tour : \n\n")
            if len(round_name) > 20:
                print("La valeur saisie est trop longue !\n")
                return self.get_round_name()
            return round_name

        except SyntaxError:
            print("Erreur de syntaxe, veuillez recommencer !\n")
            return self.get_round_name()

    def get_score_player(self, id_player):
        try:
            score_player = float(input(f"Saisissez le score pour le joueur avec l'ID : {id_player}"
                                       f" : score (1 or 0 or 0.5)\n\n"))
            if len(str(score_player)) > 4:
                return self.get_score_player(id_player)
            return score_player

        except ValueError:  # if string is passed as int
            print("Saisissez seulement des nombres !\n\n")
            return self.get_score_player(id_player)
