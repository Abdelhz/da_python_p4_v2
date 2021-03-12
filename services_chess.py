def sorting_list(list_of_players):
    list_players_sorted = sorted(list_of_players, key=lambda player: player.ranking)
    list_players_sorted.reverse()
    return list_players_sorted


def create_pairs(list_players_sorted):
    list_of_players_ids = []
    for player in list_players_sorted:
        list_of_players_ids.append(player.id_player)

    list_of_pairs = []
    for i in range(0, (int(len(list_of_players_ids)/2))):
        pair_players = [list_of_players_ids[i], list_of_players_ids[i + (int(len(list_of_players_ids)/2))]]
        list_of_pairs.append(pair_players)
    return list_of_pairs



