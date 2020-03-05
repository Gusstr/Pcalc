#input_hand1 = input()
#input_hand2 = input()
#hälften är på input resten är på handö
#table = ["h4", "h7", "hA", "s3", "h8"]

#if input_hand1[1] = "a" or "k" or "q" or "t":
 #   print()
#else:
#    hand1 = input_hand1

# return antingen None eller en lista av integers [5, 8, 10, 12, 13]

hand1 = ("h", 6)
hand2 = ("c", 5)

table = [
    ('h', 4),
    ('h', 7),
    ('h', 14),
    ('s', 3),
    ('h', 8)
]

def flush(cards_on_table, card_on_hand1, card_on_hand2):
    c = h = s = d = 0
    h_flush = []
    s_flush = []
    c_flush = []
    d_flush = []
    for x in cards_on_table:
        if ([x][0][0]) == "h":
            h = h + 1
            h_flush.append([x][0][1])
        elif ([x][0][0]) == "s":
            s = s + 1
            s_flush.append([x][0][1])
        elif ([x][0][0]) == "d":
            d = d + 1
            d_flush.append([x][0][1])
        elif ([x][0][0]) == "c":
            c = c + 1
            c_flush.append([x][0][1])
    print(h, s, d, c)
    if card_on_hand1[0] == "h":
        h = h + 1
        h_flush.append(card_on_hand1[1])
    if card_on_hand1[0] == "c":
        c = c + 1
        c_flush.append(card_on_hand1[1])
    if card_on_hand1[0] == "s":
        s = s + 1
        s_flush.append(card_on_hand1[1])
    if card_on_hand1[0] == "d":
        d = d + 1
        d_flush.append(card_on_hand1[1])
    if card_on_hand2[0] == "h":
        h = h + 1
        h_flush.append(card_on_hand2[1])
    if card_on_hand2[0] == "c":
        c = c + 1
        c_flush.append(card_on_hand2[1])
    if card_on_hand2[0] == "s":
        s = s + 1
        s_flush.append(card_on_hand2[1])
    if card_on_hand2[0] == "d":
        d = d + 1
        d_flush.append(card_on_hand2[1])
    if h > 4:
        h_flush.sort(reverse=True)
        return h_flush
    if s > 4:
        s_flush.sort(reverse=True)
        return s_flush
    if c > 4:
        c_flush.sort(reverse=True)
        return c_flush
    if d > 4:
        d_flush.sort(reverse=True)
        return d_flush

def streight(cards_on_table, card_on_hand1, card_on_hand2):
    all_cards = []
    all_cards.append(card_on_hand1[1])
    all_cards.append(card_on_hand2[1])
    for x in cards_on_table:
        all_cards.append([x][0][1])
    all_cards.sort()
    for y in all_cards:
        if y + 1 in all_cards:
            if y + 2 in all_cards:
                if y + 3 in all_cards:
                    if y + 4 in all_cards:
                        highest_flush = y+4
    return highest_flush

            
def one_pair(cards_on_table, card_on_hand1, card_on_hand2):
    all_cards = []
    all_cards.append(card_on_hand1[1])
    all_cards.append(card_on_hand2[1])
    for x in cards_on_table:
        all_cards.append([x][0][1])
    all_cards.sort()
    for x in all_cards:
        #måste hitta ett sätt där den ser om x finns två gånger i ala_cards
        if x & x in all_cards:
            print("pair")

        
print(streight(table, hand1, hand2))

