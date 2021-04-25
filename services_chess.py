def sorting_list_score(list_of_players):
    list_players_sorted_score = sorted(list_of_players, key=lambda player: player.score)
    list_players_sorted_score.reverse()
    return list_players_sorted_score


def create_all_pairs(list_players_sorted):
    list_all_pairs = []
    for i in range(0, int(len(list_players_sorted)-1)):
        for j in range(i+1, int(len(list_players_sorted))):
            pair_players = [list_players_sorted[i], list_players_sorted[j]]
            list_all_pairs.append(pair_players)
    return list_all_pairs

# list_done_pairs = []


def create_pairs(list_players_sorted, list_all_pairs, list_done_pairs):
    list_of_players_ids = []
    for player in list_players_sorted:
        list_of_players_ids.append(player.id_player)

    list_of_pairs = []
    for i in range(0, (int(len(list_players_sorted)/2))):
        pair_players = [list_players_sorted[i], list_players_sorted[i + (int(len(list_players_sorted)/2))]]
        list_of_pairs.append(pair_players)
        list_done_pairs.append(pair_players)
        for pair in list_all_pairs:
            pair_player_reversed = [pair_players[1], pair_players[0]]
            if pair_players == pair:
                list_all_pairs.remove(pair)
            elif pair_player_reversed == pair:
                list_all_pairs.remove(pair)
    return list_of_pairs


def create_new_pairs(list_players_sorted, list_done_pairs):
    list_of_pairs = []
    list_players_tempo = list_players_sorted
    while list_players_tempo:
        i = 0
        pair_players = [list_players_sorted[i], list_players_sorted[i+1]]
        for pair in list_done_pairs:
            pair_player_reversed = [pair_players[1], pair_players[0]]
            if pair_players == pair:
                pair_players == [list_players_sorted[i], list_players_sorted[i+2]]
                list_players_tempo.remove(list_players_sorted[i])
                list_players_tempo.remove(list_players_sorted[i+2])
                list_of_pairs.append(pair_players)
                list_done_pairs.append(pair_players)
            elif pair_player_reversed == pair:
                pair_players == [list_players_sorted[i], list_players_sorted[i + 2]]
                list_players_tempo.remove(list_players_sorted[i])
                list_players_tempo.remove(list_players_sorted[i + 2])
                list_of_pairs.append(pair_players)
                list_done_pairs.append(pair_players)
            else:
                list_players_tempo.remove(list_players_sorted[i])
                list_players_tempo.remove(list_players_sorted[i + 1])
                list_of_pairs.append(pair_players)
                list_done_pairs.append(pair_players)
    return list_of_pairs
