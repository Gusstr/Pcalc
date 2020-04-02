import handingcards
import translator
import winner_check

amount_of_wins = 0
amount_of_splits = 0

for lol in range(1000):
    cards = translator.card_translator(handingcards.card_randomizer(), handingcards.player_cards)
    winner = winner_check.winner_check(cards[0], cards[1])
    if winner == 0:
        amount_of_wins += 1
    if winner == 50:
        amount_of_splits += 1
    print(lol)

win_percentage = amount_of_wins / 10
split_precentage = amount_of_splits / 10

win_precentage_over_avarage = win_percentage - (100 / (handingcards.number_of_opponents + 1))
win_precentage_over_avarage = win_precentage_over_avarage * 10
print("chansen att vinna är:", win_percentage,"%")
print(win_precentage_over_avarage)
print("chansen för split är:", split_precentage,"%")

    



#fixa str flush i inputpart 
#str flush returner inte 0 även när det inte är straight flush