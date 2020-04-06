def main_function(card1, card2, number_of_opponents):
    import handingcards
    import translator
    import winner_check

    amount_of_wins = 0
    amount_of_splits = 0

    for round in range(1000):
        returns_of_player_card_giver = handingcards.player_card_giver(card1, card2)
        cards = translator.card_translator(handingcards.card_randomizer(returns_of_player_card_giver[0], number_of_opponents), returns_of_player_card_giver[1])
        winner = winner_check.winner_check(cards[0], cards[1])
        if winner == 0:
            amount_of_wins += 1
        if winner == 50:
            amount_of_splits += 1
        print(round)

    win_percentage = amount_of_wins / 10
    split_precentage = amount_of_splits / 10

    win_precentage_over_avarage = win_percentage - (100 / (number_of_opponents + 1))
    print("chansen att vinna är:", win_percentage,"%")
    print(win_precentage_over_avarage)
    print("chansen för split är:", split_precentage,"%")
    return win_percentage, win_precentage_over_avarage, split_precentage



