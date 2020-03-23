import inputpart
import översättare

flop = [("h", 4),("s", 4),("c", 9),("d", 9),("h", 14)]

winner_index = 100
win_on_full_house = []
winner_triss_value = 0
winner_pair_value = 0

for player_index, player in enumerate(översättare.handingcards.opponents):
    triss_value = 0
    pair_value = 0
    if inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[0] == inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[2] and inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[3] == inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[4]:
        triss_value = inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[0]
        pair_value = inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[3]
    elif inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[0] == inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[1] and inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[2] == inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[4]:
        triss_value = inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[2]
        pair_value = inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[0]

    if triss_value != 0 and win_on_full_house == []:
        win_on_full_house = inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
        winner_triss_value = triss_value
        winner_pair_value = pair_value
        winner_index = player_index

    elif triss_value != 0 and win_on_full_house != []:
        if triss_value > winner_triss_value:
            win_on_full_house = inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
            winner_triss_value = triss_value
            winner_pair_value = pair_value
            winner_index = player_index
        if triss_value == winner_triss_value:
            if pair_value > winner_pair_value:
                win_on_full_house = inputpart.pairs(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                winner_triss_value = triss_value
                winner_pair_value = pair_value
            if pair_value == winner_pair_value and winner_index == 0:
                winner_index = 50

print(winner_index)
print(winner_pair_value)
print(winner_triss_value)

