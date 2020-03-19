#input_hand1 = input()
#input_hand2 = input()
#hälften är på input resten är på handö
#table = ["h4", "h7", "hA", "s3", "h8"]

#if input_hand1[1] = "a" or "k" or "q" or "t":
 #   print()
#else:
#    hand1 = input_hand1

# return antingen None eller en lista av integers [5, 8, 10, 12, 13]

hand1 = ("h", 3)
hand2 = ("h", 4)

table = [
    ('s', 4),
    ('h', 5),
    ('h', 6),
    ('c', 11),
    ('h', 2)
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
    else:
        return False

def str_flush(cards_on_table, card_on_hand1, card_on_hand2):
    if flush(cards_on_table, card_on_hand1, card_on_hand2) != 0:
        all_cards = []
        final_hand = []
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
                            final_hand = [y+4, y+3, y+2, y+1, y]
                            return final_hand
    else:
        return False


def streight(cards_on_table, card_on_hand1, card_on_hand2):
    all_cards = []
    all_cards.append(card_on_hand1[1])
    all_cards.append(card_on_hand2[1])
    for x in cards_on_table:
        all_cards.append([x][0][1])
    all_cards.sort()
    highest_streight = 0
    for y in all_cards:
        if y + 1 in all_cards:
            if y + 2 in all_cards:
                if y + 3 in all_cards:
                    if y + 4 in all_cards:
                        highest_streight = y+4
    return highest_streight
    

def pairs(cards_on_table, card_on_hand1, card_on_hand2):
    all_cards = []
    final_hand = []
    all_cards.append(card_on_hand1[1])
    all_cards.append(card_on_hand2[1])
    for x in cards_on_table:
        all_cards.append([x][0][1])
    all_cards.sort(reverse=True)

    kickers = 5
    for x in all_cards:
        if all_cards.count(x) == 2:
            final_hand.append(x)
            kickers = 3
        if all_cards.count(x) == 3:
            final_hand.append(x)
            kickers = 2
        if all_cards.count(x) == 4:
            final_hand.append(x)
            kickers = 1
 
    if len(final_hand) > 5:
        if len(final_hand) == 6:
            del final_hand[-1] 
        elif len(final_hand) == 7:
            del final_hand[-1]
            del final_hand[-2]
        
    print(all_cards)
    check_kickers = 1
    if len(final_hand) == 4 or len(final_hand) == 5:
        if len(final_hand) == 4:
            if final_hand[0] == final_hand[1] and final_hand[2] == final_hand[3]:
                check_kickers = 1
                kickers = 1
            else:
                check_kickers = 1
                kickers = 1
        elif len(final_hand) == 5:
            if final_hand[0] == final_hand[1] and final_hand[2] == final_hand[3] == final_hand[4] or final_hand[0] == final_hand[1] == final_hand[2] and final_hand[3] == final_hand[4]:
                check_kickers = 2
                kickers = 0
            else:
                del final_hand[-1]
                check_kickers = 1
                kickers = 1
        
    if check_kickers == 1:
        if kickers == 5:
            final_hand.append(all_cards[0])
            final_hand.append(all_cards[1])
            final_hand.append(all_cards[2])
            final_hand.append(all_cards[3])
            final_hand.append(all_cards[4])
        if kickers == 3:
            all_cards.remove(final_hand[0])
            all_cards.remove(final_hand[1])

            final_hand.append(all_cards[0])
            final_hand.append(all_cards[1])
            final_hand.append(all_cards[2])
        elif kickers == 2:
            all_cards.remove(final_hand[0])
            all_cards.remove(final_hand[1])
            all_cards.remove(final_hand[2])

            final_hand.append(all_cards[0])
            final_hand.append(all_cards[1])
        elif kickers == 1:
            all_cards.remove(final_hand[0])
            all_cards.remove(final_hand[1])
            all_cards.remove(final_hand[2])
            all_cards.remove(final_hand[3])

            final_hand.append(all_cards[0])
    return final_hand

print(str_flush(table, hand1, hand2))



print(pairs(table, hand1, hand2))
