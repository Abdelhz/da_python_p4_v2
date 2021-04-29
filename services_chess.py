def sorting_list_score(list_of_players):
    list_players_sorted_score = sorted(list_of_players, key=lambda player: player.score)
    list_players_sorted_score.reverse()
    return list_players_sorted_score


def create_pairs(list_players_sorted, list_done_pairs):
    list_of_pairs = []
    for i in range(0, (int(len(list_players_sorted)/2))):
        pair_players = [list_players_sorted[i], list_players_sorted[i + (int(len(list_players_sorted)/2))]]
        list_of_pairs.append(pair_players)
        list_done_pairs.append(pair_players)
    return list_of_pairs, list_done_pairs


def create_new_pairs(list_players_sorted, list_done_pairs):
    list_of_pairs = []
    list_players_tempo = list_players_sorted
    while int(len(list_players_tempo)) > 0:
        i = 0
        pair_players = [list_players_tempo[i], list_players_tempo[i+1]]
        if int(len(list_players_tempo)) > 2:
            for pair in list_done_pairs:
                if (pair_players[0].id_player == pair[0].id_player and pair_players[1].id_player == pair[1].id_player)\
                        or (pair_players[1].id_player == pair[0].id_player
                            and pair_players[0].id_player == pair[1].id_player):
                    pair_players = [list_players_tempo[i], list_players_tempo[i+2]]
                    list_of_pairs.append(pair_players)
                    list_done_pairs.append(pair_players)
                    list_players_tempo.remove(list_players_tempo[i])
                    list_players_tempo.remove(list_players_tempo[i + 2])
                else:
                    list_of_pairs.append(pair_players)
                    list_done_pairs.append(pair_players)
                    list_players_tempo.remove(list_players_tempo[i])
                    list_players_tempo.remove(list_players_tempo[i + 1])

        list_of_pairs.append(pair_players)
        list_done_pairs.append(pair_players)
        list_players_tempo.remove(list_players_tempo[i])
        list_players_tempo.remove(list_players_tempo[i + 1])
    return list_of_pairs
