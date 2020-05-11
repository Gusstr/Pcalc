def card_translator(cards, player):
    translated_flop = []
    for index_card , card in enumerate(cards[0]):
        translated_flop.append([cards[0][index_card][0], cards[0][index_card][1]])

    for card_index, card in enumerate(translated_flop):
        if translated_flop[card_index][1] == "2":
            translated_flop[card_index].remove("2")
            translated_flop[card_index].insert(1, 2)

        elif translated_flop[card_index][1] == "3":
            translated_flop[card_index].remove("3")
            translated_flop[card_index].insert(1, 3)

        elif translated_flop[card_index][1] == "4":
            translated_flop[card_index].remove("4")
            translated_flop[card_index].insert(1, 4)

        elif translated_flop[card_index][1] == "5":
            translated_flop[card_index].remove("5")
            translated_flop[card_index].insert(1, 5)

        elif translated_flop[card_index][1] == "6":
            translated_flop[card_index].remove("6")
            translated_flop[card_index].insert(1, 6)

        elif translated_flop[card_index][1] == "7":
            translated_flop[card_index].remove("7")
            translated_flop[card_index].insert(1, 7)

        elif translated_flop[card_index][1] == "8":
            translated_flop[card_index].remove("8")
            translated_flop[card_index].insert(1, 8)

        elif translated_flop[card_index][1] == "9":
            translated_flop[card_index].remove("9")
            translated_flop[card_index].insert(1, 9)

        elif translated_flop[card_index][1] == "T":
            translated_flop[card_index].remove("T")
            translated_flop[card_index].insert(1, 10)

        elif translated_flop[card_index][1] == "J":
            translated_flop[card_index].remove("J")
            translated_flop[card_index].insert(1, 11)

        elif translated_flop[card_index][1] == "Q":
            translated_flop[card_index].remove("Q")
            translated_flop[card_index].insert(1, 12)

        elif translated_flop[card_index][1] == "K":
            translated_flop[card_index].remove("K")
            translated_flop[card_index].insert(1, 13)

        elif translated_flop[card_index][1] == "A":
            translated_flop[card_index].remove("A")
            translated_flop[card_index].insert(1, 14)

    for list_index, the_list in enumerate(translated_flop):
        translated_flop[list_index] = tuple(translated_flop[list_index])
    
    translated_opponents = []
    for index_card , card in enumerate(cards[1]):
        translated_opponents.append([cards[1][index_card][0], cards[1][index_card][1]])

    translated_player_cards = []
    for index_player_cards, card in enumerate(player):
        translated_player_cards.append([player[index_player_cards][0], player[index_player_cards][1]])
    translated_opponents.insert(0, translated_player_cards)    

    for opponent_index, opponent in enumerate(translated_opponents):
        for card_index, card in enumerate(translated_opponents[opponent_index]):
            if translated_opponents[opponent_index][card_index][1] == "2":
                translated_opponents[opponent_index][card_index].remove("2")
                translated_opponents[opponent_index][card_index].insert(1, 2)

            elif translated_opponents[opponent_index][card_index][1] == "3":
                translated_opponents[opponent_index][card_index].remove("3")
                translated_opponents[opponent_index][card_index].insert(1, 3)

            elif translated_opponents[opponent_index][card_index][1] == "4":
                translated_opponents[opponent_index][card_index].remove("4")
                translated_opponents[opponent_index][card_index].insert(1, 4)

            elif translated_opponents[opponent_index][card_index][1] == "5":
                translated_opponents[opponent_index][card_index].remove("5")
                translated_opponents[opponent_index][card_index].insert(1, 5)

            elif translated_opponents[opponent_index][card_index][1] == "6":
                translated_opponents[opponent_index][card_index].remove("6")
                translated_opponents[opponent_index][card_index].insert(1, 6)

            elif translated_opponents[opponent_index][card_index][1] == "7":
                translated_opponents[opponent_index][card_index].remove("7")
                translated_opponents[opponent_index][card_index].insert(1, 7)

            elif translated_opponents[opponent_index][card_index][1] == "8":
                translated_opponents[opponent_index][card_index].remove("8")
                translated_opponents[opponent_index][card_index].insert(1, 8)

            elif translated_opponents[opponent_index][card_index][1] == "9":
                translated_opponents[opponent_index][card_index].remove("9")
                translated_opponents[opponent_index][card_index].insert(1, 9)

            elif translated_opponents[opponent_index][card_index][1] == "T":
                translated_opponents[opponent_index][card_index].remove("T")
                translated_opponents[opponent_index][card_index].insert(1, 10)

            elif translated_opponents[opponent_index][card_index][1] == "J":
                translated_opponents[opponent_index][card_index].remove("J")
                translated_opponents[opponent_index][card_index].insert(1, 11)

            elif translated_opponents[opponent_index][card_index][1] == "Q":
                translated_opponents[opponent_index][card_index].remove("Q")
                translated_opponents[opponent_index][card_index].insert(1, 12)

            elif translated_opponents[opponent_index][card_index][1] == "K":
                translated_opponents[opponent_index][card_index].remove("K")
                translated_opponents[opponent_index][card_index].insert(1, 13)

            elif translated_opponents[opponent_index][card_index][1] == "A":
                translated_opponents[opponent_index][card_index].remove("A")
                translated_opponents[opponent_index][card_index].insert(1, 14)


    for opponent_index, opponent in enumerate(translated_opponents):
        for card_index, card in enumerate(translated_opponents[opponent_index]):
            translated_opponents[opponent_index][card_index] = tuple(translated_opponents[opponent_index][card_index])

    return translated_flop, translated_opponents

