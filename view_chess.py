# View
class View:
    def get_name(self):
        try:
            name = input("Give a name !")
            if len(name) > 20:
                return self.get_name()
            return name

        except SyntaxError:
            return self.get_name()

    def get_ranking(self):
        try:
            ranking = int(input("Give player ranking !"))
            return ranking

        except SyntaxError:  # if string is passed as int
            print("Enter only numbers !")
            return self.get_ranking()

    def get_elo(self):
        try:
            elo = int(input("Give player elo !"))
            return elo

        except ValueError:  # if string is passed as int
            print("Enter only numbers !")
            return self.get_elo()

    def get_gender(self):
        try:
            gender = input("Give a gender !")
            if len(gender) > 6:
                return self.get_gender()
            return gender

        except ValueError:
            return self.get_gender()

    def get_date_of_birth(self):
        try:
            date_of_birth = int(input("Give player date of birth as : mmddyyyy"))
            if len(str(date_of_birth)) > 8:
                return self.get_date_of_birth()
            return date_of_birth

        except ValueError:  # if string is passed as int
            print("Enter only numbers !")
            return self.get_date_of_birth()

    def get_id_player(self):
        try:
            id_player = input("Give a 4 digits ID")
            if len(id_player) > 4:
                return self.get_id_player()
            return id_player

        except ValueError:  # if string is passed as int
            print("Enter only numbers !")
            return self.get_id_player()
