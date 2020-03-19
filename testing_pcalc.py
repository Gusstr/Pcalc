import översättare
import inputpart

flop = [("h", 4),("s", 10),("h", 7),("h", 6),("c", 10)]


def winner_check ():
    winner_index = 100
    win_on_strflush = []
    for player_index, player in enumerate(översättare.handingcards.opponents):
        for card in range(5):
            if inputpart.str_flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]) != False:
                if win_on_strflush == []:
                    win_on_strflush = inputpart.str_flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                    winner_index = player_index
                    break
                if win_on_strflush != []:
                    if inputpart.str_flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[card] > win_on_strflush[card]:
                        win_on_strflush = inputpart.str_flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                        winner_index = player_index
                        break
                    elif inputpart.str_flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[card] < win_on_strflush[card]:
                        break
    if winner_index != 100:
        return winner_index

    win_on_flsuh = []
    for player_index, player in enumerate(översättare.handingcards.opponents):
        for card in range(5):
            if inputpart.flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]) != False:
                if win_on_flsuh == []:
                    win_on_flsuh = inputpart.flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                    winner_index = player_index
                    break
                if win_on_flsuh != []:
                    if inputpart.flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[card] > win_on_flsuh[card]:
                        win_on_flsuh = inputpart.flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                        winner_index = player_index
                        break
                    elif inputpart.flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[card] < win_on_flsuh[card]:
                        break
                
                                    #om fler har exakt samma kort, t.ex flush på floppen?
    if winner_index != 100:
        return winner_index
    #fortsätt med resten av händerna 
print(winner_check())
                
#for player_index, player in enumerate(översättare.handingcards.opponents):
 #   print(inputpart.streight(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]))

