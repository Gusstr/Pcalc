import inputpart

def winner_check (flop, opponents):
    winner_index = 100
    win_on_strflush = []
    for player_index, player in enumerate(opponents):
        for card in range(5):
            if inputpart.str_flush(flop, opponents[player_index][0], opponents[player_index][1]) != 0:
                if win_on_strflush == []:
                    win_on_strflush = inputpart.str_flush(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_index = player_index
                    break
                if win_on_strflush != []:
                    if inputpart.str_flush(flop, opponents[player_index][0], opponents[player_index][1])[card] > win_on_strflush[card]:
                        win_on_strflush = inputpart.str_flush(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                        break
                    elif inputpart.str_flush(flop, opponents[player_index][0], opponents[player_index][1])[card] < win_on_strflush[card]:
                        break
                    elif card == 4 and inputpart.str_flush(flop, opponents[player_index][0], opponents[player_index][1])[card] == win_on_strflush[card]:
                        if winner_index == 0:
                            winner_index = 50

    if winner_index != 100:
        return winner_index

    win_on_four_of_a_kind = []
    for player_index, player in enumerate(opponents):
        if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[3]:
            if win_on_four_of_a_kind == []:
                win_on_four_of_a_kind = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                winner_index = player_index
            if win_on_four_of_a_kind != []:
                if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] > win_on_four_of_a_kind[0]:
                    win_on_four_of_a_kind = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_index = player_index
                if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == win_on_four_of_a_kind[0]:
                    if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[4] > win_on_four_of_a_kind[4]:
                        win_on_four_of_a_kind = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                    if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[4] == win_on_four_of_a_kind[4] and winner_index == 0:
                        winner_index = 50
                    if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[4] == win_on_four_of_a_kind[4]:
                        winner_index = player_index
    if winner_index != 100:
        return winner_index

    win_on_full_house = []
    winner_triss_value = 0
    winner_pair_value = 0
    for player_index, player in enumerate(opponents):
        triss_value = 0
        pair_value = 0
        if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[2] and inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[3] == inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[4]:
            triss_value = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0]
            pair_value = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[3]
        elif inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[1] and inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[2] == inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[4]:
            triss_value = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[2]
            pair_value = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0]

        if triss_value != 0 and win_on_full_house == []:
            win_on_full_house = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
            winner_triss_value = triss_value
            winner_pair_value = pair_value
            winner_index = player_index

        elif triss_value != 0 and win_on_full_house != []:
            if triss_value > winner_triss_value:
                win_on_full_house = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                winner_triss_value = triss_value
                winner_pair_value = pair_value
                winner_index = player_index
            if triss_value == winner_triss_value:
                if pair_value > winner_pair_value:
                    win_on_full_house = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_triss_value = triss_value
                    winner_pair_value = pair_value
                if pair_value == winner_pair_value and winner_index == 0:
                    winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_flsuh = []
    for player_index, player in enumerate(opponents):
        for card in range(5):
            if inputpart.flush(flop, opponents[player_index][0], opponents[player_index][1]) != False:
                if win_on_flsuh == []:
                    win_on_flsuh = inputpart.flush(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_index = player_index
                    break
                if win_on_flsuh != []:
                    if inputpart.flush(flop, opponents[player_index][0], opponents[player_index][1])[card] > win_on_flsuh[card]:
                        win_on_flsuh = inputpart.flush(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                        break
                    elif inputpart.flush(flop, opponents[player_index][0], opponents[player_index][1])[card] < win_on_flsuh[card]:
                        break
                    elif card == 4 and inputpart.flush(flop, opponents[player_index][0], opponents[player_index][1])[card] == win_on_flsuh[card]:
                        if winner_index == 0:
                            winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_straight = 0
    for player_index, player in enumerate(opponents):
        if inputpart.straight(flop, opponents[player_index][0], opponents[player_index][1]) > win_on_straight:
            win_on_straight = inputpart.straight(flop, opponents[player_index][0], opponents[player_index][1])
            winner_index = player_index
        elif inputpart.straight(flop, opponents[player_index][0], opponents[player_index][1]) == win_on_straight and winner_index == 0:
            winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_three_of_a_kind = []
    for player_index, player in enumerate(opponents):
        for card in range(2):
            if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[2]:
                if win_on_three_of_a_kind == []:
                    win_on_three_of_a_kind = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_index = player_index
                    break
                if win_on_three_of_a_kind != []:
                    if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] > win_on_three_of_a_kind[0]:
                        win_on_three_of_a_kind = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                        break
                    if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == win_on_three_of_a_kind[0]:
                        if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card + 3] > win_on_three_of_a_kind[card + 3]:
                            win_on_three_of_a_kind = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                            winner_index = player_index
                            break
                        elif inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card + 3] < win_on_three_of_a_kind[card + 3]:
                            break
                        elif card == 1 and inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card + 3] == win_on_three_of_a_kind[card + 3]:
                            if winner_index == 0:
                                winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_two_pair = []
    for player_index, player in enumerate(opponents):
        if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[1] and inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[2] == inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[3]:
            if win_on_two_pair == []:
                win_on_two_pair = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                winner_index = player_index
            elif win_on_two_pair != []:
                for card in range(5):
                    if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] > win_on_two_pair[card]:
                        win_on_two_pair = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                        break
                    if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] < win_on_two_pair[card]:
                        break
                    if card == 4 and inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] == win_on_two_pair[card]:
                        if winner_index == 0:
                            winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_pair = []
    for player_index, player in enumerate(opponents):
        if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[1]:
            if win_on_pair == []:
                win_on_pair = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                winner_index = player_index
            elif win_on_pair != []:
                for card in range(5):
                    if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] > win_on_pair[card]:
                        win_on_pair = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                        break
                    if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] < win_on_pair[card]:
                        break
                    if card == 4 and inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] == win_on_pair[card]:
                        if winner_index == 0:
                            winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_high_card = []
    for player_index, player in enumerate(opponents):
        if win_on_high_card == []:
            win_on_high_card = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
        elif win_on_high_card != []:
            for card in range(5):
                if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] > win_on_high_card[card]:
                    win_on_high_card = inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_index = player_index
                    break
                if inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] < win_on_high_card[card]:
                    break
                if card == 4 and inputpart.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] == win_on_high_card[card]:
                    if winner_index == 0:
                        winner_index = 50
    return winner_index
            
                



    


