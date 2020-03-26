import inputpart
import översättare

flop = [("h", 7), ("s", 5), ("d", 12), ("c", 12), ("s", 9)]

winner_index = 100
win_on_high_card = []
for player_index, player in enumerate(översättare.handingcards.opponents):
    if win_on_high_card == []:
        win_on_high_card = inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
    elif win_on_high_card != []:
        for card in range(5):
            if inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[card] > win_on_high_card[card]:
                win_on_high_card = inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                winner_index = player_index
                break
            if inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[card] < win_on_high_card[card]:
                break
            if card == 4 and inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[card] == win_on_high_card[card]:
                if winner_index == 0:
                    winner_index = 50

print(winner_index)
print(win_on_high_card)

