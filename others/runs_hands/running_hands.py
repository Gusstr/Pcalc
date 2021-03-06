def main_function(card1, card2, number_of_opponents):
    from others.giving_cards import handing_cards
    from others.giving_cards import translator
    from others.winner_of_the_hand import winner_check

    amount_of_wins = 0
    amount_of_splits = 0

    for round in range(1000):
        returns_of_player_card_giver = handing_cards.player_card_giver(card1, card2)
        cards = translator.card_translator(handing_cards.card_randomizer(returns_of_player_card_giver[0], number_of_opponents), returns_of_player_card_giver[1])
        winner = winner_check.winner_check(cards[0], cards[1])
        if winner == 0:
            amount_of_wins += 1
        if winner == 50:
            amount_of_splits += 1

    win_percentage = amount_of_wins / 10
    split_precentage = amount_of_splits / 10

    win_precentage_over_avarage = win_percentage - (100 / (number_of_opponents + 1))
    return win_percentage, win_precentage_over_avarage, split_precentage


