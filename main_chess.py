from controller_chess import Controller


class Player:

    def __init__(self, name, ranking, elo, gender, date_of_birth, id_player, score):
        self.name = name
        self.ranking = ranking
        self.elo = elo
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.id_player = id_player
        self.score = score


player_1 = Player("paul", 1600, 500, "m", 10081990, 1403, 0)

player_2 = Player("ali", 1580, 500, "m", 18101989, 1402, 0)

player_3 = Player("abdel", 1560, 500, "m", 18021990, 1401, 0)

player_4 = Player("annie", 1540, 500, "f", 20111992, 1503, 0)

player_5 = Player("sof", 1520, 500, "m", 20101989, 1502, 0)

player_6 = Player("yas", 1500, 500, "f", 11051991, 1501, 0)

player_7 = Player("amel", 1490, 500, "f", 10081998, 1603, 0)

player_8 = Player("nour", 1480, 500, "f", 12081992, 1602, 0)

list_of_players = [player_6, player_3, player_1, player_4, player_8, player_2, player_5, player_7]
controller_ch = Controller()


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


for player in list_of_players:
    rank = str(player.ranking)
    print(rank + "\n")

list_of_matches = controller_ch.create_matchs(list_of_players)

for match in list_of_matches:
    print(match)
