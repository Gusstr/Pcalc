import random
def player_card_giver(card1, card2,):
    cards = [["h2", "d2", "c2", "s2"],
            ["h3", "d3", "c3", "s3"],
            ["h4", "d4", "c4", "s4"],
            ["h5", "d5", "c5", "s5"], 
            ["h6", "d6", "c6", "s6"],
            ["h7", "d7", "c7", "s7"], 
            ["h8", "d8", "c8", "s8"], 
            ["h9", "d9", "c9", "s9"], 
            ["hT", "dT", "cT", "sT"], 
            ["hJ", "dJ", "cJ", "sJ"], 
            ["hQ", "dQ", "cQ", "sQ"], 
            ["hK", "dK", "cK", "sK"], 
            ["hA", "dA", "cA", "sA"]]

    player_cards = [card1, card2]

    for index_row, row in enumerate(cards):
        for index_card, card in enumerate(row):
            if card1 == card:
                del cards[index_row][index_card]
            if card2 == card:
                del cards[index_row][index_card]
    return cards, player_cards

def card_randomizer(original_cards, num_opponents):
    usable_cards = []
    for index_row, row in enumerate(original_cards):
        usable_cards.append([])
        for index_card, card in enumerate(original_cards[index_row]):
            usable_cards[index_row].append(original_cards[index_row][index_card])
    flop = []
    opponents = []
    for player in range(num_opponents):
        opponents.append([])
        for cards_per_hand in range(2):
            while True:
                row_number = random.randint(0, 12)
                if len(usable_cards[row_number]) != 0:
                    break
            card_number = random.randint(0, len(usable_cards[row_number]) - 1)

            opponents[player].append([usable_cards[row_number][card_number][0], usable_cards[row_number][card_number][1]])
            del usable_cards[row_number][card_number]

    for flop_card in range(5):
        while True:
            row_number = random.randint(0, 12)
            if len(usable_cards[row_number]) != 0:
                break
        card_number = random.randint(0, len(usable_cards[row_number]) - 1)
        flop.append(usable_cards[row_number][card_number])
        del usable_cards[row_number][card_number]
    return flop, opponents



