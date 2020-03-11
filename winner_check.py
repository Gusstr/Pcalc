import översättare
import inputpart
winner_hand =[]

for player_index, player in enumerate(översättare.handingcards.opponents):
    if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]) == "No flush":
        print("ingen flush")
    elif inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]) != "No flush":
        print(inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]))
        x = 1
#def winner_check ():
    #for player_index, player in enumerate(översättare.handingcards.opponents):
        #if inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1]) != "No flush":
            #if winner_hand == []:
                #winner_hand = inputpart.flush(översättare.translated_flop, översättare.handingcards.opponents[player_index][0], översättare.handingcards.opponents[player_index][1])

    


