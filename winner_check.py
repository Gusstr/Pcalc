import determine_handstrength

def winner_check (flop, opponents):
    winner_index = 100
    win_on_strflush = []
    for player_index, player in enumerate(opponents):
        for card in range(5):
            if determine_handstrength.str_flush(flop, opponents[player_index][0], opponents[player_index][1]) != 0:
                if win_on_strflush == []:
                    win_on_strflush = determine_handstrength.str_flush(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_index = player_index
                    break
                if win_on_strflush != []:
                    if determine_handstrength.str_flush(flop, opponents[player_index][0], opponents[player_index][1])[card] > win_on_strflush[card]:
                        win_on_strflush = determine_handstrength.str_flush(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                        break
                    elif determine_handstrength.str_flush(flop, opponents[player_index][0], opponents[player_index][1])[card] < win_on_strflush[card]:
                        break
                    elif card == 4 and determine_handstrength.str_flush(flop, opponents[player_index][0], opponents[player_index][1])[card] == win_on_strflush[card]:
                        if winner_index == 0:
                            winner_index = 50

    if winner_index != 100:
        return winner_index

    win_on_four_of_a_kind = []
    for player_index, player in enumerate(opponents):
        if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[3]:
            if win_on_four_of_a_kind == []:
                win_on_four_of_a_kind = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                winner_index = player_index
            if win_on_four_of_a_kind != []:
                if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] > win_on_four_of_a_kind[0]:
                    win_on_four_of_a_kind = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_index = player_index
                if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == win_on_four_of_a_kind[0]:
                    if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[4] > win_on_four_of_a_kind[4]:
                        win_on_four_of_a_kind = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                    if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[4] == win_on_four_of_a_kind[4] and winner_index == 0:
                        winner_index = 50
                    if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[4] == win_on_four_of_a_kind[4]:
                        winner_index = player_index
    if winner_index != 100:
        return winner_index

    win_on_full_house = []
    winner_triss_value = 0
    winner_pair_value = 0
    for player_index, player in enumerate(opponents):
        triss_value = 0
        pair_value = 0
        if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[2] and determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[3] == determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[4]:
            triss_value = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0]
            pair_value = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[3]
        elif determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[1] and determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[2] == determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[4]:
            triss_value = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[2]
            pair_value = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0]

        if triss_value != 0 and win_on_full_house == []:
            win_on_full_house = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
            winner_triss_value = triss_value
            winner_pair_value = pair_value
            winner_index = player_index

        elif triss_value != 0 and win_on_full_house != []:
            if triss_value > winner_triss_value:
                win_on_full_house = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                winner_triss_value = triss_value
                winner_pair_value = pair_value
                winner_index = player_index
            if triss_value == winner_triss_value:
                if pair_value > winner_pair_value:
                    win_on_full_house = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_triss_value = triss_value
                    winner_pair_value = pair_value
                if pair_value == winner_pair_value and winner_index == 0:
                    winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_flsuh = []
    for player_index, player in enumerate(opponents):
        for card in range(5):
            if determine_handstrength.flush(flop, opponents[player_index][0], opponents[player_index][1]) != False:
                if win_on_flsuh == []:
                    win_on_flsuh = determine_handstrength.flush(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_index = player_index
                    break
                if win_on_flsuh != []:
                    if determine_handstrength.flush(flop, opponents[player_index][0], opponents[player_index][1])[card] > win_on_flsuh[card]:
                        win_on_flsuh = determine_handstrength.flush(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                        break
                    elif determine_handstrength.flush(flop, opponents[player_index][0], opponents[player_index][1])[card] < win_on_flsuh[card]:
                        break
                    elif card == 4 and determine_handstrength.flush(flop, opponents[player_index][0], opponents[player_index][1])[card] == win_on_flsuh[card]:
                        if winner_index == 0:
                            winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_straight = 0
    for player_index, player in enumerate(opponents):
        if determine_handstrength.straight(flop, opponents[player_index][0], opponents[player_index][1]) > win_on_straight:
            win_on_straight = determine_handstrength.straight(flop, opponents[player_index][0], opponents[player_index][1])
            winner_index = player_index
        elif determine_handstrength.straight(flop, opponents[player_index][0], opponents[player_index][1]) == win_on_straight and winner_index == 0:
            winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_three_of_a_kind = []
    for player_index, player in enumerate(opponents):
        for card in range(2):
            if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[2]:
                if win_on_three_of_a_kind == []:
                    win_on_three_of_a_kind = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_index = player_index
                    break
                if win_on_three_of_a_kind != []:
                    if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] > win_on_three_of_a_kind[0]:
                        win_on_three_of_a_kind = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                        break
                    if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == win_on_three_of_a_kind[0]:
                        if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card + 3] > win_on_three_of_a_kind[card + 3]:
                            win_on_three_of_a_kind = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                            winner_index = player_index
                            break
                        elif determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card + 3] < win_on_three_of_a_kind[card + 3]:
                            break
                        elif card == 1 and determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card + 3] == win_on_three_of_a_kind[card + 3]:
                            if winner_index == 0:
                                winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_two_pair = []
    for player_index, player in enumerate(opponents):
        if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[1] and determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[2] == determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[3]:
            if win_on_two_pair == []:
                win_on_two_pair = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                winner_index = player_index
            elif win_on_two_pair != []:
                for card in range(5):
                    if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] > win_on_two_pair[card]:
                        win_on_two_pair = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                        break
                    if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] < win_on_two_pair[card]:
                        break
                    if card == 4 and determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] == win_on_two_pair[card]:
                        if winner_index == 0:
                            winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_pair = []
    for player_index, player in enumerate(opponents):
        if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[0] == determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[1]:
            if win_on_pair == []:
                win_on_pair = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                winner_index = player_index
            elif win_on_pair != []:
                for card in range(5):
                    if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] > win_on_pair[card]:
                        win_on_pair = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                        winner_index = player_index
                        break
                    if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] < win_on_pair[card]:
                        break
                    if card == 4 and determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] == win_on_pair[card]:
                        if winner_index == 0:
                            winner_index = 50
    if winner_index != 100:
        return winner_index

    win_on_high_card = []
    for player_index, player in enumerate(opponents):
        if win_on_high_card == []:
            win_on_high_card = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
        elif win_on_high_card != []:
            for card in range(5):
                if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] > win_on_high_card[card]:
                    win_on_high_card = determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])
                    winner_index = player_index
                    break
                if determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] < win_on_high_card[card]:
                    break
                if card == 4 and determine_handstrength.pairs(flop, opponents[player_index][0], opponents[player_index][1])[card] == win_on_high_card[card]:
                    if winner_index == 0:
                        winner_index = 50
    return winner_index
            
                



    


