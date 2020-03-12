import handingcards

#tranlating flop to tuple
translated_flop = []

for index_card , card in enumerate(handingcards.flop):
    translated_flop.append([handingcards.flop[index_card][0], handingcards.flop[index_card][1]])

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





#translating player cards to tuple
translated_player_cards = []

for index_player_cards, card in enumerate(handingcards.player_cards):
    translated_player_cards.append([handingcards.player_cards[index_player_cards][0], handingcards.player_cards[index_player_cards][1]])


for card_index, card in enumerate(translated_player_cards):
    if translated_player_cards[card_index][1] == "2":
        translated_player_cards[card_index].remove("2")
        translated_player_cards[card_index].insert(1, 2)
    
    elif translated_player_cards[card_index][1] == "3":
        translated_player_cards[card_index].remove("3")
        translated_player_cards[card_index].insert(1, 3)
    
    elif translated_player_cards[card_index][1] == "4":
        translated_player_cards[card_index].remove("4")
        translated_player_cards[card_index].insert(1, 4)

    elif translated_player_cards[card_index][1] == "5":
        translated_player_cards[card_index].remove("5")
        translated_player_cards[card_index].insert(1, 5)
    
    elif translated_player_cards[card_index][1] == "6":
        translated_player_cards[card_index].remove("6")
        translated_player_cards[card_index].insert(1, 6)
    
    elif translated_player_cards[card_index][1] == "7":
        translated_player_cards[card_index].remove("7")
        translated_player_cards[card_index].insert(1, 7)

    elif translated_player_cards[card_index][1] == "8":
        translated_player_cards[card_index].remove("8")
        translated_player_cards[card_index].insert(1, 8)
    
    elif translated_player_cards[card_index][1] == "9":
        translated_player_cards[card_index].remove("9")
        translated_player_cards[card_index].insert(1, 9)

    elif translated_player_cards[card_index][1] == "T":
        translated_player_cards[card_index].remove("T")
        translated_player_cards[card_index].insert(1, 10)
    
    elif translated_player_cards[card_index][1] == "J":
        translated_player_cards[card_index].remove("J")
        translated_player_cards[card_index].insert(1, 11)
    
    elif translated_player_cards[card_index][1] == "Q":
        translated_player_cards[card_index].remove("Q")
        translated_player_cards[card_index].insert(1, 12)

    elif translated_player_cards[card_index][1] == "K":
        translated_player_cards[card_index].remove("K")
        translated_player_cards[card_index].insert(1, 13)
    
    elif translated_player_cards[card_index][1] == "A":
        translated_player_cards[card_index].remove("A")
        translated_player_cards[card_index].insert(1, 14)


for list_index, the_list in enumerate(translated_player_cards):
    translated_player_cards[list_index] = tuple(translated_player_cards[list_index])

#translated opponents 
#is already translated just need making A = 14

for opponent_index, opponent in enumerate(handingcards.opponents):
    for card_index, card in enumerate(handingcards.opponents[opponent_index]):
        if handingcards.opponents[opponent_index][card_index][1] == "2":
            handingcards.opponents[opponent_index][card_index].remove("2")
            handingcards.opponents[opponent_index][card_index].insert(1, 2)

        elif handingcards.opponents[opponent_index][card_index][1] == "3":
            handingcards.opponents[opponent_index][card_index].remove("3")
            handingcards.opponents[opponent_index][card_index].insert(1, 3)

        elif handingcards.opponents[opponent_index][card_index][1] == "4":
            handingcards.opponents[opponent_index][card_index].remove("4")
            handingcards.opponents[opponent_index][card_index].insert(1, 4)

        elif handingcards.opponents[opponent_index][card_index][1] == "5":
            handingcards.opponents[opponent_index][card_index].remove("5")
            handingcards.opponents[opponent_index][card_index].insert(1, 5)

        elif handingcards.opponents[opponent_index][card_index][1] == "6":
            handingcards.opponents[opponent_index][card_index].remove("6")
            handingcards.opponents[opponent_index][card_index].insert(1, 6)

        elif handingcards.opponents[opponent_index][card_index][1] == "7":
            handingcards.opponents[opponent_index][card_index].remove("7")
            handingcards.opponents[opponent_index][card_index].insert(1, 7)

        elif handingcards.opponents[opponent_index][card_index][1] == "8":
            handingcards.opponents[opponent_index][card_index].remove("8")
            handingcards.opponents[opponent_index][card_index].insert(1, 8)

        elif handingcards.opponents[opponent_index][card_index][1] == "9":
            handingcards.opponents[opponent_index][card_index].remove("9")
            handingcards.opponents[opponent_index][card_index].insert(1, 9)

        elif handingcards.opponents[opponent_index][card_index][1] == "T":
            handingcards.opponents[opponent_index][card_index].remove("T")
            handingcards.opponents[opponent_index][card_index].insert(1, 10)

        elif handingcards.opponents[opponent_index][card_index][1] == "J":
            handingcards.opponents[opponent_index][card_index].remove("J")
            handingcards.opponents[opponent_index][card_index].insert(1, 11)
        
        elif handingcards.opponents[opponent_index][card_index][1] == "Q":
            handingcards.opponents[opponent_index][card_index].remove("Q")
            handingcards.opponents[opponent_index][card_index].insert(1, 12)
        
        elif handingcards.opponents[opponent_index][card_index][1] == "K":
            handingcards.opponents[opponent_index][card_index].remove("K")
            handingcards.opponents[opponent_index][card_index].insert(1, 13)
        
        elif handingcards.opponents[opponent_index][card_index][1] == "A":
            handingcards.opponents[opponent_index][card_index].remove("A")
            handingcards.opponents[opponent_index][card_index].insert(1, 14)


for opponent_index, opponent in enumerate(handingcards.opponents):
    for card_index, card in enumerate(handingcards.opponents[opponent_index]):
        handingcards.opponents[opponent_index][card_index] = tuple(handingcards.opponents[opponent_index][card_index])


handingcards.opponents.insert(0, translated_player_cards)

print(handingcards.opponents)
print(translated_flop)
