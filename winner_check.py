import översättare
import inputpart

for player_index, player in enumerate(översättare.handingcards.opponents):
    if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]) == "No flush":
        print("ingen flush")
    elif inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]) != "No flush":
        print(inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]))
        x = 1

def winner_check ():
    win_on_flsuh = []
    winner_index = 100
    for player_index, player in enumerate(översättare.handingcards.opponents):
        if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]) != "No flush":
            if win_on_flsuh == []:
                win_on_flsuh = inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                winner_index = player_index
            if win_on_flsuh != []:
                if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[0] > win_on_flsuh[0]:
                    win_on_flsuh = inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                    winner_index = player_index
                if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[0] == win_on_flsuh[0]:
                    if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[1] > win_on_flsuh[1]:
                        win_on_flsuh = inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                        winner_index = player_index
                    if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[1] == win_on_flsuh[1]:
                        if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[2] > win_on_flsuh[2]:
                            win_on_flsuh = inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                            winner_index = player_index
                        if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[2] == win_on_flsuh[2]:
                            if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[3] > win_on_flsuh[3]:
                                win_on_flsuh = inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                                winner_index = player_index
                            if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[3] == win_on_flsuh[3]:
                                if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])[4] > win_on_flsuh[4]:
                                    win_on_flsuh = inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])
                                    winner_index = player_index 
                                    #om fler har exakt samma kort, t.ex flush på floppen?
    if winner_index != 100:
        return winner_index
    #fortsätt med resten av händerna 
winner_check()
                
for player_index, player in enumerate(översättare.handingcards.opponents):
    print(inputpart.streight(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]))


    


