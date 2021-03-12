from controller_chess import Controller

list_of_players = []
controller_ch = Controller()

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

for player in list_of_players:
    rank = str(player.ranking)
    print(rank + "\n")

list_of_matches = controller_ch.create_matchs(list_of_players)

for match in list_of_matches:
    print(match)