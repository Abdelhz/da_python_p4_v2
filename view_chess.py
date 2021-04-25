# View
class View:
    def get_name(self):
        try:
            name = input("Give a name !\n\n")
            if len(name) > 20:
                print("Name is too long !\n")
                return self.get_name()
            return name

        except SyntaxError:
            print("Error in syntax, please retry !\n")
            return self.get_name()

    def get_ranking(self):
        try:
            ranking = int(input("Give player ranking !\n\n"))
            if len(str(ranking)) > 4:
                print("Value entered is too long !\n")
                return self.get_ranking()
            return ranking

        except ValueError:  # if string is passed as int
            print("Enter only numbers !\n\n")
            return self.get_ranking()

    def get_gender(self):
        try:
            gender = input("Give a gender as Male : m or Female : f \n\n")
            if len(gender) > 1:
                print("Value entered is too long !\n")
                return self.get_gender()
            return gender

        except SyntaxError:
            print("Error in syntax, please retry !\n")
            return self.get_gender()

    def get_date_of_birth(self):
        try:
            date_of_birth = input("Give player date of birth as : mm/dd/yyyy\n\n")
            if len(date_of_birth) > 10:
                print("Date of birth is too long !\n")
                return self.get_date_of_birth()
            return date_of_birth

        except SyntaxError:  # if string is passed as int
            print("Write date of birth as shown !\n\n")
            return self.get_date_of_birth()

    def get_id_player(self):
        try:
            id_player = int(input("Give a 4 digits ID\n\n"))
            if len(str(id_player)) > 4:
                print("Value entered is too long !\n")
                return self.get_id_player()
            return id_player

        except ValueError:  # if int is passed as string
            print("Enter only numbers !\n\n")
            return self.get_id_player()

    def get_tournament_name(self):
        try:
            tournament_name = input("Give a tournament name !\n\n")
            if len(tournament_name) > 20:
                print("Tournament name is too long !\n")
                return self.get_tournament_name()
            return tournament_name

        except SyntaxError:
            print("Error in syntax, please retry !\n")
            return self.get_tournament_name()

    def get_number_rounds(self):
        try:
            number_of_rounds = int(input("Give number of rounds !\n\n"))
            if len(str(number_of_rounds)) > 1:
                print("Number of rounds is too big !\n")
                return self.get_number_rounds()
            return number_of_rounds

        except ValueError:  # if int is passed as string
            print("Enter only numbers !\n\n")
            return self.get_number_rounds()

    def get_tournament_location(self):
        try:
            tournament_location = input("Give a tournament location !\n\n")
            if len(tournament_location) > 20:
                print("Tournament location is too long !\n")
                return self.get_tournament_location()
            return tournament_location

        except SyntaxError:
            print("Error in syntax, please retry !\n")
            return self.get_tournament_location()

    def get_tournament_date_start(self):
        try:
            tournament_date_start = input("Give tournament start date as : mm/dd/yyyy\n\n")
            if len(tournament_date_start) > 10:
                print("Value entered is too long !\n")
                return self.get_tournament_date_start()
            return tournament_date_start

        except SyntaxError:  # if not written correctly
            print("Write start date as shown !\n\n")
            return self.get_tournament_date_start()

    def get_tournament_date_end(self):
        try:
            tournament_date_end = input("Give tournament end date as : mm/dd/yyyy\n\n")
            if len(tournament_date_end) > 10:
                print("Value entered is too long !\n")
                return self.get_tournament_date_end()
            return tournament_date_end

        except SyntaxError:  # if not written correctly
            print("Write end date as shown !\n\n")
            return self.get_tournament_date_end()

    def get_number_days(self):
        try:
            number_days = int(input("Give number of days !\n\n"))
            if len(str(number_days)) > 2:
                print("Number of days is too long !\n")
                return self.get_number_days()
            return number_days

        except ValueError:  # if int is passed as string
            print("Enter only numbers !\n\n")
            return self.get_number_days()

    def get_number_players(self):
        try:
            number_players = int(input("Give the number of players participating :\n\n"))
            if len(str(number_players)) > 2:
                print("Number of players is too big !\n")
                return self.get_number_players()
            return number_players

        except ValueError:  # if int is passed as string
            print("Enter only numbers !\n\n")
            return self.get_number_players()

    def get_round_start_time(self):
        try:
            round_start_time = input("Give tournament date as : mm/dd/yyyy hh:mm\n\n")
            if len(round_start_time) > 16:
                return self.get_round_start_time()
            return round_start_time

        except SyntaxError:  # if not written correctly
            print("Write as shown !\n\n")
            return self.get_round_start_time()

    def get_round_end_time(self):
        try:
            round_end_time = input("Give tournament date as : mm/dd/yyyy hh:mm\n\n")
            if len(round_end_time) > 16:
                return self.get_round_end_time()
            return round_end_time

        except SyntaxError:  # if not written correctly
            print("Write as shown !\n\n")
            return self.get_round_end_time()

    def get_round_name(self):
        try:
            round_name = input("Give a tournament name !\n\n")
            if len(round_name) > 20:
                print("Round name is too long !\n")
                return self.get_round_name()
            return round_name

        except SyntaxError:
            print("Error in syntax, please retry !\n")
            return self.get_round_name()

    def get_score_player(self, id_player):
        try:
            score_player = float(input(f"Give the score for the player {id_player} : 1 or 0 or 0.5\n\n"))
            if len(str(score_player)) > 4:
                return self.get_score_player()
            return score_player

        except ValueError:  # if string is passed as int
            print("Enter only numbers !\n\n")
            return self.score_player()

