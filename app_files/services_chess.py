def sorting_list_score(list_of_players):
    list_players_sorted_score = sorted(list_of_players,
                                       key=lambda player:
                                       (player.score, player.ranking))
    list_players_sorted_score.reverse()
    return list_players_sorted_score


def create_pairs(list_players_sorted, list_done_pairs):
    list_of_pairs = []
    for i in range(0, (int(len(list_players_sorted) / 2))):
        condition = (int(len(list_players_sorted) / 2))
        pair_players = [list_players_sorted[i], list_players_sorted[i +
                                                                    condition]]
        list_of_pairs.append(pair_players)
        list_done_pairs.append(pair_players)
    return list_of_pairs, list_done_pairs


def create_new_pairs(list_players_sort, list_done_pairs):
    list_of_pairs = []
    list_player_tempo = list_players_sort.copy()
    while int(len(list_player_tempo)) > 0:
        i = 0
        pair_players = [list_player_tempo[i], list_player_tempo[i + 1]]
        if int(len(list_player_tempo)) > 2:
            pair_exist = False
            for pair in list_done_pairs:
                if (pair_players[0].id_player == pair[0].id_player and
                    pair_players[1].id_player == pair[1].id_player) \
                        or (pair_players[1].id_player == pair[0].id_player
                            and pair_players[0].id_player ==
                            pair[1].id_player):
                    pair_exist = True
                    pair_players = [list_player_tempo[i],
                                    list_player_tempo[i + 2]]
                    list_of_pairs.append(pair_players)
                    list_done_pairs.append(pair_players)
                    list_player_tempo.remove(list_player_tempo[i])
                    list_player_tempo.remove(list_player_tempo[i + 1])
                    break
                pass
            if not pair_exist:
                pair_players = [list_player_tempo[i], list_player_tempo[i + 1]]
                list_of_pairs.append(pair_players)
                list_done_pairs.append(pair_players)
                list_player_tempo.remove(list_player_tempo[i])
                list_player_tempo.remove(list_player_tempo[i])
            pass
        else:
            list_of_pairs.append(pair_players)
            list_done_pairs.append(pair_players)
            list_player_tempo.remove(list_player_tempo[i])
            list_player_tempo.remove(list_player_tempo[i])

    return list_of_pairs, list_done_pairs
