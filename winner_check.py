import översättare
import inputpart

def winner_check ():
    win_on_flsuh = []
    winner_index = False
    for player_index, player in enumerate(översättare.handingcards.opponents):
        for card in range(5):
            if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]) != 0:
                if win_on_flsuh == []:
                    win_on_flsuh = inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                    winner_index = player_index
                    break
                if win_on_flsuh != []:
                    if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[card] > win_on_flsuh[card]:
                        win_on_flsuh = inputpart.flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                        winner_index = player_index
                        break
                    elif inputpart.flush(flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[card] < win_on_flsuh[card]:
                        break
                
                                    #om fler har exakt samma kort, t.ex flush på floppen?
    if winner_index != False:
        return winner_index
    #fortsätt med resten av händerna 
print(winner_check())
                
#for player_index, player in enumerate(översättare.handingcards.opponents):
 #   print(inputpart.streight(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]))


    


