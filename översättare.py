import handingcards

print(handingcards.flop)

translated_flop = []

for index_card , card in enumerate(handingcards.flop):
    print(handingcards.flop[index_card])
    translated_flop.append((handingcards.flop[index_card][0], handingcards.flop[index_card][1]))

print(translated_flop)