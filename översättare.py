import handingcards

#tranlating flop to tuple
translated_flop = []

for index_card , card in enumerate(handingcards.flop):
    translated_flop.append([handingcards.flop[index_card][0], handingcards.flop[index_card][1]])

print(translated_flop)

for card_index, card in enumerate(translated_flop):
    if translated_flop[card_index][1] == "T":
        translated_flop[card_index].remove("T")
        translated_flop[card_index].insert(1, "10")
    
    elif translated_flop[card_index][1] == "J":
        translated_flop[card_index].remove("J")
        translated_flop[card_index].insert(1, "11")
    
    elif translated_flop[card_index][1] == "Q":
        translated_flop[card_index].remove("Q")
        translated_flop[card_index].insert(1, "12")

    elif translated_flop[card_index][1] == "K":
        translated_flop[card_index].remove("K")
        translated_flop[card_index].insert(1, "13")
    
    elif translated_flop[card_index][1] == "A":
        translated_flop[card_index].remove("A")
        translated_flop[card_index].insert(1, "14")
    
print(translated_flop)
for list_index, the_list in enumerate(translated_flop):
    translated_flop[list_index] = tuple(translated_flop[list_index])

print(translated_flop)




#translating player cards to tuple
translated_player_cards = []

for index_player_cards, card in enumerate(handingcards.player_cards):
    translated_player_cards.append([handingcards.player_cards[index_player_cards][0], handingcards.player_cards[index_player_cards][1]])

print(translated_player_cards)

for card_index, card in enumerate(translated_player_cards):
    if translated_player_cards[card_index][1] == "T":
        translated_player_cards[card_index].remove("T")
        translated_player_cards[card_index].insert(1, "10")
    
    elif translated_player_cards[card_index][1] == "J":
        translated_player_cards[card_index].remove("J")
        translated_player_cards[card_index].insert(1, "11")
    
    elif translated_player_cards[card_index][1] == "Q":
        translated_player_cards[card_index].remove("Q")
        translated_player_cards[card_index].insert(1, "12")

    elif translated_player_cards[card_index][1] == "K":
        translated_player_cards[card_index].remove("K")
        translated_player_cards[card_index].insert(1, "13")
    
    elif translated_player_cards[card_index][1] == "A":
        translated_player_cards[card_index].remove("A")
        translated_player_cards[card_index].insert(1, "14")

print(translated_player_cards)

for list_index, the_list in enumerate(translated_player_cards):
    translated_player_cards[list_index] = tuple(translated_player_cards[list_index])

print(translated_player_cards)
#translated opponents 
#is already translated just need making A = 14

for opponent_index, opponent in enumerate(handingcards.opponents):
    for card_index, card in enumerate(handingcards.opponents[opponent_index]):
        if handingcards.opponents[opponent_index][card_index][1] == "T":
            handingcards.opponents[opponent_index][card_index].remove("T")
            handingcards.opponents[opponent_index][card_index].insert(1, "10")

        elif handingcards.opponents[opponent_index][card_index][1] == "J":
            handingcards.opponents[opponent_index][card_index].remove("J")
            handingcards.opponents[opponent_index][card_index].insert(1, "11")
        
        elif handingcards.opponents[opponent_index][card_index][1] == "Q":
            handingcards.opponents[opponent_index][card_index].remove("Q")
            handingcards.opponents[opponent_index][card_index].insert(1, "12")
        
        elif handingcards.opponents[opponent_index][card_index][1] == "K":
            handingcards.opponents[opponent_index][card_index].remove("K")
            handingcards.opponents[opponent_index][card_index].insert(1, "13")
        
        elif handingcards.opponents[opponent_index][card_index][1] == "A":
            handingcards.opponents[opponent_index][card_index].remove("A")
            handingcards.opponents[opponent_index][card_index].insert(1, "14")

print(handingcards.opponents)

for opponent_index, opponent in enumerate(handingcards.opponents):
    for card_index, card in enumerate(handingcards.opponents[opponent_index]):
        handingcards.opponents[opponent_index][card_index] = tuple(handingcards.opponents[opponent_index][card_index])

print(handingcards.opponents)